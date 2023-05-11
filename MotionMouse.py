import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            index_x, index_y = None, None
            thumb_x, thumb_y = None, None
            middle_x, middle_y = None, None
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y

            if thumb_x and index_x and abs(index_y - thumb_y) < 10:
                pyautogui.click()
                pyautogui.sleep(1)

            if middle_x and index_x and abs(index_y - middle_y) < 10:
                pyautogui.rightClick()
                pyautogui.sleep(1)

    cv2.imshow('Motion Mouse', frame)
    cv2.waitKey(1)
