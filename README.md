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
  A dynamic workout planner that allows users to select exercises such as:
  - Squats
  - Push-ups
  - Bicep Curls
  - And more

  Users can also configure target **sets** and **repetitions**.

- **Live Video Streaming**  
  Real-time webcam integration directly in the browser using `streamlit-webrtc`.

- **AI Pose Detection**  
  MediaPipe Pose Landmarker is integrated for advanced body and movement tracking.

- **Exercise Tracking**  
  Built-in AI logic for **Squats**, including:
  - Knee angle tracking
  - Back angle tracking
  - Squat depth detection
  - Exercise status tracking

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11** | Programming Language |
| **Streamlit** | Web Application Framework |
| **Streamlit-WebRTC** | Real-time Video Streaming |
| **OpenCV** | Computer Vision |
| **MediaPipe** | AI Pose Detection |
| **SQLite3** | Local Database |

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/rajath-j/ai-gym-coach.git
cd ai-gym-coach
```

### 2. Create a Virtual Environment

This project uses `uv` for Python environment management.

```bash
uv venv --python 3.11
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install all required Python packages:

```bash
uv pip install -r requirements.txt
```

### 4. Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

The application will then be available in your browser.

---

## Project Overview

The application combines:

- User authentication
- SQLite database management
- Workout planning
- Real-time webcam streaming
- AI-based pose detection
- Exercise angle analysis
- Exercise tracking

The goal is to provide an interactive AI-powered fitness coaching experience directly through a web browser.

---

## Author

**Rajath J**

- LinkedIn: [Rajath J](https://www.linkedin.com/in/rajath-j/)
- GitHub: [rajath-j](https://github.com/rajath-j)

---

## Project

**AI Real-time GYM Coach**

> A browser-based AI fitness trainer for real-time exercise tracking and workout assistance.