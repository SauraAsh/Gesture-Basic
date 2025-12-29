# Gesture Control - High Performance

Control your **mouse cursor with one hand** using hand gestures.

## Features
- High scaling: small hand movements → large cursor movements
- Automatic click with pinch gesture (thumb + index)
- Smooth movement similar to a real mouse
- Optional camera preview

## Step-by-Step Setup

### 1️⃣ Install Python
- Download Python 3.11+ (64-bit) from [python.org](https://www.python.org/downloads/)
- Check **Add Python to PATH**
- Verify:
```bash
python --version
2️⃣ Setup Virtual Environment (Optional)
python -m venv gesture_env
gesture_env\Scripts\activate   # Windows
# source gesture_env/bin/activate  # Linux/Mac
3️⃣ Install Dependencies
pip install --upgrade pip
pip install opencv-python mediapipe pyautogui
Or via requirements.txt:
pip install -r requirements.txt
4️⃣ Run the Script
python gesture_basic.py
Move index finger to move cursor
Pinch gesture to click
Press ESC to exit
5️⃣ Optional Tuning
MULTIPLIER → distance multiplier
SMOOTH → smooth factor for cursor
CLICK_DELAY → delay between auto clicks
Notes
Ensure sufficient lighting for hand tracking
### **4️⃣ .gitignore**
pycache/ *.pyc *.pyo .env .DS_Store