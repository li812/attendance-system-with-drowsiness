#train_image.py

def train():
    import os
    import time
    import cv2
    import numpy as np
    from PIL import Image
    from threading import Thread

    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
        faces = []
        Ids = []
        for imagePath in imagePaths:
            pilImage = Image.open(imagePath).convert('L')
            imageNp = np.array(pilImage, 'uint8')
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def TrainImages():
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            faces, Id = getImagesAndLabels("TrainingImage")
            Thread(target=recognizer.train(faces, np.array(Id))).start()
            Thread(target=counter_img("TrainingImage")).start()
            recognizer.save("TrainingImageLabel" + os.sep + "Trainner.yml")
            print("All Images")
        except Exception as e:
            print("An error occurred during training:", e)

    def counter_img(path):
        imgcounter = 1
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            print(str(imgcounter) + " Images Trained", end="\r")
            time.sleep(0.008)
            imgcounter += 1

    TrainImages()


train()