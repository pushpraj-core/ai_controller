import cv2
import mediapipe as mp
import pyautogui
import math
import time
import os
from pynput.mouse import Button, Controller as MouseController
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# --- 1. SETUP ---
mouse = MouseController()
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'hand_landmarker.task')

# SYSTEM CALIBRATION
sw, sh = pyautogui.size()
plocX, plocY = 0, 0
clocX, clocY = 0, 0
ALPHA = 0.20 

# ACTION TRACKING
last_right_click = 0
last_left_click = 0
CLICK_COOLDOWN = 0.6  
last_zoom_time = 0
last_palm_y = 0 # This ensures scrolling stays at the last position

CONNECTIONS = [
    (0,1), (1,2), (2,3), (3,4), (0,5), (5,6), (6,7), (7,8),
    (9,10), (10,11), (11,12), (13,14), (14,15), (15,16),
    (17,18), (18,19), (19,20), (5,9), (9,13), (13,17), (0,17)
]

options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1
)

cap = cv2.VideoCapture(0)

# --- 2. THE ENGINE ---
with vision.HandLandmarker.create_from_options(options) as landmarker:
    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        
        frame = cv2.flip(frame, 1) 
        h, w, _ = frame.shape
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        result = landmarker.detect_for_video(mp_image, int(time.time() * 1000))

        # --- PERSISTENCE LOGIC ---
        # If hand is detected, update everything. 
        # If NOT detected, the code does nothing, so the mouse "stays" put.
        if result.hand_landmarks:
            for hand_lms in result.hand_landmarks:
                # 1. DRAW SKELETON
                for edge in CONNECTIONS:
                    p1, p2 = hand_lms[edge[0]], hand_lms[edge[1]]
                    cv2.line(frame, (int(p1.x*w), int(p1.y*h)), (int(p2.x*w), int(p2.y*h)), (0, 255, 0), 2)

                # 2. ALIASES & DISTANCES
                thm, idx, mid, rng, pnk = hand_lms[4], hand_lms[8], hand_lms[12], hand_lms[16], hand_lms[20]
                dist_idx = math.hypot(idx.x - thm.x, idx.y - thm.y) 
                dist_mid = math.hypot(mid.x - thm.x, mid.y - thm.y) 
                
                # 3. MOUSE MOVEMENT (Only happens when hand is visible)
                tx, ty = idx.x * sw, idx.y * sh
                clocX = (ALPHA * tx) + ((1 - ALPHA) * plocX)
                clocY = (ALPHA * ty) + ((1 - ALPHA) * plocY)
                mouse.position = (clocX, clocY)
                plocX, plocY = clocX, clocY 

                # 4. GESTURES with DELAY
                # Left Click
                if dist_idx < 0.06:
                    if time.time() - last_left_click > CLICK_COOLDOWN:
                        pyautogui.click(button='left')
                        last_left_click = time.time()
                
                # Right Click
                elif dist_mid < 0.06:
                    if time.time() - last_right_click > CLICK_COOLDOWN:
                        pyautogui.click(button='right')
                        last_right_click = time.time()

                # 5. SCROLLING (Palm Logic)
                is_palm = (idx.y < hand_lms[6].y and mid.y < hand_lms[10].y and rng.y < hand_lms[14].y)
                if is_palm:
                    cv2.putText(frame, "SCROLLING", (50, 50), 1, 2, (255, 255, 0), 2)
                    if last_palm_y != 0:
                        diff = last_palm_y - mid.y
                        if abs(diff) > 0.03:
                            mouse.scroll(0, int(diff * 12)) 
                    last_palm_y = mid.y
                else:
                    last_palm_y = 0 # Reset when palm is closed
        else:
            # OPTIONAL: Visual cue that tracking is lost
            cv2.putText(frame, "HAND OUT OF RANGE - FROZEN", (50, h-50), 1, 1.5, (0, 0, 255), 2)
            # Important: We do NOT reset plocX/plocY here, so it resumes from the same spot.
            last_palm_y = 0 

        cv2.imshow('Persistent AI Controller v40', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()