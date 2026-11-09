# AI Real-time GYM Coach

A real-time, browser-based AI fitness trainer built with **Streamlit** and **WebRTC**. This application allows users to log in, configure personalized workout plans, and use live video for AI-powered exercise tracking.

---

## Current Features

- **User Authentication**  
  A secure login wall that creates and tracks unique user sessions.

- **Database Integration**  
  A local SQLite backend (`data.db`) that manages user profiles and initializes exercise history tracking.

- **Custom UI & Styling**  
  An enhanced Streamlit interface featuring a custom dark theme, CSS injection, and the **Adobe Clean** font.

- **Interactive Sidebar**  
  A dynamic workout planner that allows users to select exercises, configure target **sets**, and set **repetitions**. Supported exercises include:
  - Squats
  - Push-ups
  - Biceps curls (Dumbbell)
  - Shoulder press
  - Lunges

- **Live Video Streaming & Processing**  
  Real-time webcam integration directly in the browser using `streamlit-webrtc`. Custom video processing handles frame-by-frame analysis with a threaded lock system to pass live metrics securely to the UI.

- **AI Pose Detection & Visual Feedback**  
  MediaPipe Pose Landmarker is integrated for advanced body and movement tracking. The application dynamically draws pose skeletons, connection lines, and real-time metric text overlays directly on the live video feed.

- **Exercise Tracking & Form Analysis**  
  Built-in AI logic actively evaluates form and counts reps for specific exercises:
  - **Squats:** Knee/back angle tracking and squat depth detection (Good Depth / Too High).
  - **Push-ups:** Elbow angle tracking, body alignment, and hip position status.
  - **Biceps Curls:** Elbow angle tracking, shoulder stability, and swing detection.
  - **Shoulder Press:** Elbow angle tracking, arm extension, and back arch status.
  - **Lunges:** Front knee angle, torso angle, and balance status.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11** | Programming Language |
| **Streamlit** | Web Application Framework |
| **Streamlit-WebRTC** | Real-time Video Streaming |
| **OpenCV** | Computer Vision & Video Overlays |
| **MediaPipe** | AI Pose Detection |
| **SQLite3** | Local Database |

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/rajath-j/ai-gym-coach.git](https://github.com/rajath-j/ai-gym-coach.git)
cd ai-gym-coach