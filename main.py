import math
import cv2
import mediapipe as mp
import pyautogui as pag
import time


screen_width, screen_height = pag.size()

mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
cap = cv2.VideoCapture(1)



def main():
    while True:
        ct = 0
        pt = 0
        success, img = cap.read()
        img = cv2.flip(img, 1)
        cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
        vidh, vidw, vidz = img.shape

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data = hands.process(imgRGB)
        ct = time.time()
        fps = int(round(1 / (ct - pt)))
        pt = ct
        cv2.putText(img, "FPS : {}".format(fps), (0, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
        break_out = False
        if data.multi_hand_landmarks:
            for x in data.multi_hand_landmarks:
                pointx = x.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
                pointy = x.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
                middlex = x.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x
                middley = x.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
                thumbx = x.landmark[mpHands.HandLandmark.THUMB_TIP].x
                thumby = x.landmark[mpHands.HandLandmark.THUMB_TIP].y
                cv2.circle(img, (int(pointx * vidw), int(pointy * vidh)), 10, (255, 255, 0), -1)
                cv2.circle(img, (int(thumbx * vidw), int(thumby * vidh)), 10, (255, 0, 255), -1)
                pag.moveTo(middlex * screen_width * 1.3, middley * screen_height * 1.3)

                # THANOS SNAP break if thumb and middle finger are close
                if abs(math.sqrt((middlex * screen_width - thumbx * screen_width) ** 2 + (
                        middley * screen_height - thumby * screen_height) ** 2)) < 50:
                    break_out = True
                    break

                # click if thumb finger is close to index finger
                if abs(math.sqrt((pointx * screen_width - thumbx * screen_width) ** 2 + (
                        pointy * screen_height - thumby * screen_height) ** 2)) < 50:
                    pag.click()
                    break
            if break_out:
                break

        cv2.imshow('Gesture Controlled Mouse', img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()