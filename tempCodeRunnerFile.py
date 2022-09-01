
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

                # click if thumb finger is close to index fingerggjgjgjgjjjgjj
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
