import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import time
from label_detect import classify_face
from imutils import paths
import face_recognition
import pickle


mixer.init()
sound = mixer.Sound('alarm.wav')


#face = cv2.CascadeClassifier('/media/preeth/Data/prajna_files/Drowsiness_detection/haar_cascade_files/haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
score=0
thicc=2
#faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))


i = 0
while(True):
    ret, frame = cap.read()
    height,width = frame.shape[:2]
    label = classify_face(frame)
    if(label == 'with_mask'):
        print("No Beep")
    else:
        sound.play()
        print("Beep")
        i = i + 1
        if cv2.waitKey(1) & 0xFF == ord('q') or (i == 11):
            cap.release()
            cv2.destroyAllWindows()

            exec(open('FaceDetection.py').read())
            break

    cv2.putText(frame,str(label),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)


