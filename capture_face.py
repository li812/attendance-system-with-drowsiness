#capture_face.py

def register_face(Id, name):
    import csv
    import cv2
    import os

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if not (is_number(Id) and name.isalpha()):
        if not is_number(Id):
            print("Error: ID must be numeric")
        if not name.isalpha():
            print("Error: Name must be alphabetical")
        return

    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")
    if not os.path.exists("StudentDetails"):
        os.makedirs("StudentDetails")

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Failed to open camera")
        return

    harcascadePath = "haarcascade_frontalface_default.xml"
    if not os.path.isfile(harcascadePath):
        print("Error: Haar cascade file not found")
        return
    detector = cv2.CascadeClassifier(harcascadePath)

    sampleNum = 0
    try:
        while(True):
            ret, img = cam.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                sampleNum += 1
                path = f"TrainingImage/{name}.{Id}.{sampleNum}.jpg"
                cv2.imwrite(path, gray[y:y+h, x:x+w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum > 100:
                if sampleNum > 500:
                    print("Reached maximum sample limit (500)")
                else:
                    print("Exiting on user request (press 'q')")
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()

    if sampleNum > 0:
        header = ["Id", "Name"]
        row = [Id, name]
        csv_file = "StudentDetails/StudentDetails.csv"
        mode = 'a+' if os.path.isfile(csv_file) else 'w+'
        with open(csv_file, mode, newline='') as file:
            writer = csv.writer(file)
            if mode == 'w+':
                writer.writerow(header)
            writer.writerow(row)

        print(f"Images saved for ID: {Id}, Name: {name}")


register_face("1", "John")
