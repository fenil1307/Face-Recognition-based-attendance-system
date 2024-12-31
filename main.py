
import time
import cv2
import os
import numpy as np
import face_recognition
from datetime import datetime
import pyttsx3



from geopy.geocoders import Nominatim

engin=pyttsx3.init()
path='image'
image=[]
personname=[]
mylist=os.listdir(path)
print(mylist)
for cu_img in mylist:
    current_img=cv2.imread(f'{path}/{cu_img}')
    image.append(current_img)
    personname.append(os.path.splitext(cu_img)[0])
print(personname)

def faceEncoding(image):
    encodelist=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        # print(encode)
        encodelist.append(encode)
    return encodelist

encodelistknown=faceEncoding(image)
print("ALL ENCODING DONE!!!!")

def attendance(name):
        with open("Attendance.csv", 'r+') as f:
            mydatalist=f.readlines()
            namelist=[]
            for line in mydatalist:
                entry=line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                    time_now=datetime.now()
                    tstr=time_now.strftime('%H:%M:%S')
                    dstr=time_now.strftime('%d/%m/%Y')
                    f.writelines(f'{name},{tstr},{dstr}\n')

cap = cv2.VideoCapture(0)
frame_skip = 5
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process every nth frame
    if frame_count % frame_skip == 0:
        faces_small = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces_small = cv2.cvtColor(faces_small, cv2.COLOR_BGR2RGB)
        facescurrentframe = face_recognition.face_locations(faces_small)
        encodesCurrentFrame = face_recognition.face_encodings(faces_small, facescurrentframe)

        for encodeface, faceloc in zip(encodesCurrentFrame, facescurrentframe):
            match = face_recognition.compare_faces(encodelistknown, encodeface)
            facedis = face_recognition.face_distance(encodelistknown, encodeface)
            matchindex = np.argmin(facedis)

            if match[matchindex]:
                name = personname[matchindex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
                attendance(name)

    cv2.imshow("camera", frame)
    frame_count += 1

    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()







