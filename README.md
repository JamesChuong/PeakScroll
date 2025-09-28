# 🏔️ PeakScroll

*Because your feed should match your mood.*  

---

## 🚀 Overview  
This project pioneers the next generation of **personalized content consumption** by combining **computer vision**, **emotion detection**, and **browser automation**.  

The system runs a lightweight vision model locally using **OpenCV** to read facial expressions in real time. If the system detects that a user is **bored, unhappy, or frustrated** while watching short-form content on **YouTube Shorts** or **Instagram Reels**, it automatically sends a command via the **Chrome DevTools Protocol** to **scroll to the next video**.  

Instead of mindlessly swiping, your content feed adapts to your **emotions**—making scrolling *smarter, healthier, and more human*.  

---

## 🌟 Key Features  
- **Real-Time Emotion Detection** – Polls user’s webcam feed to classify emotional state.  
- **Adaptive Scrolling** – If negative emotion is detected, instantly scrolls to the next reel.  
- **Local & Private** – All computer vision runs locally; no cloud uploads or data leaks.  
- **Seamless Integration** – Works directly with Chrome through the DevTools Protocol.  
- **User Interface** – Lightweight HTML/CSS panel for viewing the emotions and gestures detected.   
---

## 🙂 Gesture/Emotion Overview
- **Thumbs Up and Positive Emotions** - Likes the reel
- **Smiling** - Displays smiling emojis on the screen
- **Thumbs Down or Negative Emotions** - Scrolls down to the next reel
- **Pointing Finger Up** - Scrolls above to the last reel
___

## 🧠 Tech Stack  
- **Python** – Core logic and OpenCV-based emotion recognition.  
- **OpenCV** – Facial landmark detection and emotion classification pipeline.  
- **Chrome DevTools Protocol** – Automates browser scrolling behavior.  
- **HTML/CSS** – Configuration and user interface.  

---

## 🔮 Why This Matters  
Short-form video platforms dominate user attention—but they don’t adapt to how we actually **feel**. This project is a **step toward empathetic computing**, and the interface responds to our emotions instead of ignoring them.

Get [wifi](https://www.youtube.com/shorts/OMP3Yx-YZsw) anywhere you go.

For **investors and innovators**, this represents:  
- A **cutting-edge AI demonstration** of emotion-aware interfaces.  
- A **potential consumer product** for healthier engagement with addictive media.  
- A **blueprint for emotion-driven UX**, extendable to gaming, e-learning, and productivity.  

In short: this will **change the scrolling game forever**.  

---

## ⚡ Getting Started  

### Prerequisites  
- Python 3.9+  
- Chrome Browser  
- Webcam  

### Installation  
```bash
git clone git@github.com:JamesChuong/PeakScroll.git

cd PeakScroll
# Python 3.12 is required for certain packages and a virtual environment is recommended
python3.12 -m venv <venv-name>

# Activating the virtual environment
# Linux/MacOS
source <venv-name>/bin/activate

# Windows (This project was not tested on windows so results may vary)
.\<venv-name>\Scripts\activate

pip install -r requirements.txt

# deactivating the virtual environment
deactivate
```
### Running PeakScroll

PeakScroll uses a Flask web server to capture facial data from your webcam, determine emotions, and send data to Chrome via the DevTools Protocol.

To open Chrome with the DevTools Protocol enabled, you must locate the executable, and run it with the remote debugging port flag on.

Ensure all other instances of Chrome are completely closed (e.g., on MacOS, right-click icon and click Quit even when no windows are open).

```
mkdir /tmp/chrome-debug-profile
<path to chrome executable> --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug-profile
```

Proceed to open Instagram Reels and log in on the debug browser.

Then, in another terminal, enter the PeakScroll repository and do the following:

```bash
# Go to the web portal directory
cd web_portal
# Run the Flask app
flask run
```

The web server runs on `localhost:5000` or `127.0.0.1:5000`, make sure that that URL is open in your browser, as that is how the camera feed is processed.

Enjoy your PeakScrolling (tm pending) from the Instagram Reels tab!

---

## Contributors

- Nakul Bansal
- James Chuong
- Simon Purdon
- Micah Baker
