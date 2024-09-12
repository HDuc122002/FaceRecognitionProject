import cv2
import queryDB as db
from tkinter import messagebox

def show_interface(mode):
    cam = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainningData.yml')
    detector = cv2.CascadeClassifier('libs/haarcascade_frontalface_default.xml')

    checked_in = False

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            if confidence < 40:
                profile = db.getProfile(id)
                if profile and not checked_in:
                    action = "Check-in" if mode == "checkin" else "Check-out"
                    cv2.putText(img, f"{action}: {profile[1]}", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                    if mode == "checkin":
                        db.checkIn(id)
                    else:
                        db.checkOut(id)

                    messagebox.showinfo("Success", f"{action} thành công cho {profile[1]}")
                    checked_in = True

                    cam.release()
                    cv2.destroyAllWindows()
                    return
            else:
                cv2.putText(img, "Unknown", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow(f'{mode.capitalize()}', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
