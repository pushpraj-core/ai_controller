 NEXT GEN AI-CONTROLLER

 
Transform your webcam into a high-precision spatial mouse. No hardware, just code.


🌟 Overview
This project is a sophisticated Human-Computer Interaction (HCI) system. It bypasses traditional physical peripherals by using Computer Vision to map 21 distinct hand landmarks to real-time OS-level mouse events. Engineered for reliability, it features custom smoothing algorithms and signal persistence.




🚀 Key Technical Features
Kinematic Skeleton Mapping: Leverages the Full MediaPipe Landmarker (5.6MB model) to render a 21-node hand web with zero-latency joint tracking.

LoS (Loss-of-Signal) Persistence: Implements a state-lock mechanism that "freezes" the cursor at its last valid coordinate if the hand leaves the camera's Field of View, preventing erratic jumping.

Orthogonal Axis Logic: Intelligent gesture separation—vertical movement triggers Scrolling, while horizontal movement (when pinched) triggers Zooming.

Action Throttling: A 0.6s programmatic cooldown on clicks ensures deliberate interaction and eliminates "double-click" noise from hand jitters.




