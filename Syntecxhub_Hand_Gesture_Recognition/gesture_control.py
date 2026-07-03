import cv2
import mediapipe as mp
import math
import pyautogui 

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

cooldown_counter = 0
COOLDOWN_LIMIT = 10  

def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print("Starting Live Gesture Control... Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    gesture = "Looking for Hand..."
    action = "None"

    if cooldown_counter > 0:
        cooldown_counter -= 1

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = hand_landmarks.landmark
 
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            index_mcp = landmarks[5]
            middle_tip = landmarks[12]
            middle_mcp = landmarks[9]
            ring_tip = landmarks[16]
            ring_mcp = landmarks[13]
            pinky_tip = landmarks[20]
            pinky_mcp = landmarks[17]

            index_open = index_tip.y < index_mcp.y
            middle_open = middle_tip.y < middle_mcp.y
            ring_open = ring_tip.y < ring_mcp.y
            pinky_open = pinky_tip.y < pinky_mcp.y

            thumb_separation = get_distance(thumb_tip, index_mcp)

            if index_open and middle_open and ring_open and pinky_open:
                gesture = "Open Palm"
                action = "PLAY MEDIA"
                if cooldown_counter == 0:
                    pyautogui.press('playpause')
                    cooldown_counter = COOLDOWN_LIMIT

            elif not index_open and not middle_open and not ring_open and not pinky_open:
                if thumb_separation > 0.12:
                    gesture = "Thumbs Up"
                    action = "VOLUME UP"
                    if cooldown_counter == 0:
                        pyautogui.press('volumeup')
                        cooldown_counter = 3 
                else:
                    gesture = "Fist"
                    action = "PAUSE MEDIA"
                    if cooldown_counter == 0:
                        pyautogui.press('playpause')
                        cooldown_counter = COOLDOWN_LIMIT

    cv2.rectangle(frame, (10, 10), (400, 100), (0, 0, 0), -1)
    cv2.putText(frame, f"Gesture: {gesture}", (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame, f"Action: {action}", (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow('Hand Gesture Demo', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
