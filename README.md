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
- **Customizable Interface** – Lightweight HTML/CSS config panel for fine-tuning preferences.  

---

## 🧠 Tech Stack  
- **Python** – Core logic and OpenCV-based emotion recognition.  
- **OpenCV** – Facial landmark detection and emotion classification pipeline.  
- **Chrome DevTools Protocol** – Automates browser scrolling behavior.  
- **HTML/CSS** – Configuration and user interface.  

---

## 🔮 Why This Matters  
Short-form video platforms dominate user attention—but they don’t adapt to how we actually **feel**. This project is a **step toward empathetic computing**, where the interface responds to our emotions instead of ignoring them.  

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
git clone https://github.com/your-org/emotion-autoscroller.git
cd emotion-autoscroller
pip install -r requirements.txt
```
### Running PeakScroll

PeakScroll uses a Flask web server to capture facial data from your webcam
from the browser, determine emotions, and send data to Chrome via the DevTools Protocol
> This assumes that you are in the root directory (`\PeakScroll`)
```bash
# Go to the web portal directory
cd web_portal
# Run the Flask app
flask run
```
> The web server runs on `localhost:5000`, make sure that webcam access is enabled
