import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape


    if landmark_points:
        landmarks = landmark_points[0].landmark
        for i, landmark in enumerate(landmarks[473:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,0))
            if i == 0:
                screen_x  = screen_w / frame_w * x
                screen_y  = screen_h / frame_h * y

                pyautogui.moveTo(screen_x, screen_y, duration=0.1)

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,255))
        
        if left[0].y - left[1].y < 0.004:
            pyautogui.click()
            print("winked")
            pyautogui.sleep(1)
        # for i, landmark in enumerate(landmarks[468:473]):
        #     x = int(landmark.x * frame_w)
        #     y = int(landmark.y * frame_h)
        #     cv2.circle(frame, (x,y), 3, (0,255,0))

        

    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(1)

        # Exit mechanism
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release resources
cam.release()
cv2.destroyAllWindows()
