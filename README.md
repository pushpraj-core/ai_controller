<div align="center">
	<h1>🖐️ NEXT GEN AI-CONTROLLER</h1>
	<pre>
	 ____  ___      _      ____            _             _           
	/ __ \|__ \    | |    / __ \          | |           | |          
 | |  | |  ) | __| |__ | |  | | ___  ___| |_ __ _  ___| |_ ___ _ __
 | |  | | / / / _` / _ \| |  | |/ _ \/ __| __/ _` |/ __| __/ _ \ '__|
 | |__| |/ /_| (_| | (_) | |__| |  __/ (__| || (_| | (__| ||  __/ |   
	\____/|____(_)__,_|\___/ \____/ \___|\___|\__\__,_|\___|\__\___|_|  
	</pre>
	<p><b>Transform your webcam into a high-precision spatial mouse. No hardware, just code.</b></p>
</div>

🌟 **Overview**
This project is a sophisticated Human-Computer Interaction (HCI) system. It bypasses traditional physical peripherals by using Computer Vision to map 21 distinct hand landmarks to real-time OS-level mouse events. Engineered for reliability, it features custom smoothing algorithms and signal persistence.

---

## 🚀 Key Technical Features
- **Kinematic Skeleton Mapping:** Leverages the Full MediaPipe Landmarker (5.6MB model) to render a 21-node hand web with zero-latency joint tracking.
- **LoS (Loss-of-Signal) Persistence:** Implements a state-lock mechanism that "freezes" the cursor at its last valid coordinate if the hand leaves the camera's Field of View, preventing erratic jumping.
- **Orthogonal Axis Logic:** Intelligent gesture separation—vertical movement triggers Scrolling, while horizontal movement (when pinched) triggers Zooming.
- **Action Throttling:** A 0.6s programmatic cooldown on clicks ensures deliberate interaction and eliminates "double-click" noise from hand jitters.

---

## 🎮 Interactive Gesture Mapping
| Gesture         | Duties         | Logical Trigger                |
|-----------------|---------------|-------------------------------|
| 🏃 Love Running | Index Finger   | XY Coordinate Mapping         |
| 🖱️ Select/Drag  | Index + Thumb | Direct State Hold             |
| 👉 Right Click  | Middle + Thumb| Single Event Trigger          |
| 🖐️ Scroll      | Open Palm      | Vertical Relative Displacement|
| 🤏 Zoom         | Ring + Thumb   | Vertical Axis Scaling         |

---

## ⚡ Quick Start
1. Clone this repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`
4. Wave your hand in front of your webcam and try the gestures above!

---

## 💡 Usage Tips
- Make sure your hand is clearly visible to the camera.
- Try different lighting for best results.
- Experiment with gestures—see which ones work best for you!
- If the cursor freezes, simply bring your hand back into the frame.

---

## 🙌 Try It Yourself!
Ready to ditch your mouse? Launch the app and start controlling your computer with your hand. Share your experience or suggest new gestures!

---

<div align="center">
	<b>Made with 🤖 and ✋ for next-gen HCI</b>
</div>




