# 🏋🏻 AI Real-time GYM Coach

A real-time, browser-based AI fitness trainer built with Streamlit and WebRTC. This application allows users to log in, configure workout plans, and stream live video for exercise tracking.

## ✨ Current Features
* **User Authentication:** A secure login wall that creates and tracks unique user sessions.
* **Database Integration:** A local SQLite backend (`data.db`) that manages user profiles and initializes exercise history tracking.
* **Custom UI & Styling:** An enhanced Streamlit interface featuring a custom dark theme, CSS injection, and the Adobe Clean font.
* **Interactive Sidebar:** A dynamic workout planner to select exercises (Squats, Push-ups, Bicep Curls, etc.), target sets, and reps.
* **Live Video Streaming:** Real-time webcam integration directly in the browser using `streamlit-webrtc`.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** Streamlit
* **Video Streaming:** Streamlit-WebRTC, OpenCV
* **Database:** SQLite3

## 🚀 How to Run Locally

1. **Clone the repository:**
```bash
   git clone [https://github.com/rajath-j/ai-gym-coach.git](https://github.com/rajath-j/ai-gym-coach.git)
   cd ai-gym-coach