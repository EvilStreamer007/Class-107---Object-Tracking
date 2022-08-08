from cgi import test
import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture('/Users/chaitalishah/Desktop/Krsna_WHJ/Classes/Class-107/bb3.mp4')
tracker = cv2.TrackerCSRT_create()

returned, img = video.read()

box = cv2.selectROI("Tracker",img,False)
tracker.init(img,box)

#print(box)

def drawbox(img,box):
    (x,y,w,h) = int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)), (255,0,0), 3, 1)

    cv2.putText(img,"Tracker",(75,90),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)

def goal(img,box):
    (x,y,w,h) = int(box[0]),int(box[1]),int(box[2]),int(box[3])
    c1 = x+int(w/2) 
    c2 = y+int(h/2)

    cv2.circle(img, (c1, c2), 2, (0,0,255), 5)
    cv2.circle(img, (int(p1), int(p2)), 2, (0,0,255), 5)

    distance = math.sqrt(((c1 - p1)**2) + (c2-p2)**2)
    print(distance)

    if distance <= 20:
        cv2.putText(img, "Goal", (300,90), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]), 2, (0,0,255), 5)
        
while True:
    check, img = video.read()
    test, box = tracker.update(img)

    if test:
        drawbox(img, box)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    
    goal(img,box)

    cv2.imshow("Result", img)
    key = cv2.waitKey(25)
    
    if key == 32:
        print("Stopped")
        break

video.release()
cv2.destroyAllWindows()