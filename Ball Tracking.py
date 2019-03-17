import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    
    #Read frames from the camera
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,100,200])                 #select range of HSV values      
    upper_color = np.array([25,255,255])
    mask = cv2.inRange(hsv, lower_color, upper_color)   #mask the selected colour

    kernel = np.ones((3,3),np.uint8)                           
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)     #Morphological transformation (opening) to reduce noise

    _, contours,_ = cv2.findContours(opening,1,2)                #finding contours 

    for contour in contours:
         area = cv2.contourArea(contour)
         if area > 50:
             
             cv2.drawContours(frame, contours,-1, (200,120,0), 2)
             (x,y),radius = cv2.minEnclosingCircle(contour)
             cv2.circle(frame,(int(x),int(y)),int(radius), (255,0,0), 2)

    cv2.imshow('Result',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
