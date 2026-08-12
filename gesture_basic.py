import cv2
import mediapipe as mp
import pyautogui
import time

# ===== CONFIG =====
MULTIPLIER = 8.0      # 1 cm hand movement = 8 cm cursor movement
SMOOTH = 0.25         # light smoothing for smoother movement
CLICK_DELAY = 0.5
pyautogui.FAILSAFE = True

# ===== SETUP =====
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

prev_x, prev_y = None, None
curr_dx, curr_dy = 0, 0
last_click = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        lm = result.multi_hand_landmarks[0].landmark
        index_tip = lm[8]
        thumb_tip = lm[4]
        index_pip = lm[6]

        finger_up = index_tip.y < index_pip.y - 0.01

        if finger_up:
            if prev_x is None:
                prev_x, prev_y = index_tip.x, index_tip.y

            dx = index_tip.x - prev_x
            dy = index_tip.y - prev_y

            target_dx = dx * pyautogui.size().width * MULTIPLIER
            target_dy = dy * pyautogui.size().height * MULTIPLIER

            curr_dx = curr_dx + (target_dx - curr_dx) * SMOOTH
            curr_dy = curr_dy + (target_dy - curr_dy) * SMOOTH

            try:
                pyautogui.moveRel(curr_dx, curr_dy)
            except pyautogui.FailSafeException:
                pass

            prev_x, prev_y = index_tip.x, index_tip.y
        else:
            prev_x, prev_y = None, None  # reset if finger is down
            curr_dx, curr_dy = 0, 0

        # Auto click (pinch)
        pinch_distance = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
        if pinch_distance < 0.03 and time.time() - last_click > CLICK_DELAY:
            pyautogui.click()
            last_click = time.time()

    # Optional preview
    cv2.imshow("Gesture Control - High Performance", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()