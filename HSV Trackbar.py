import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('image')

# create trackbars for upper HSV
cv2.createTrackbar('H_upper','image',0,180,nothing)
cv2.createTrackbar('H_lower','image',0,180,nothing)

cv2.createTrackbar('S_upper','image',0,255,nothing)
cv2.createTrackbar('S_lower','image',0,255,nothing)

cv2.createTrackbar('V_upper','image',0,255,nothing)
cv2.createTrackbar('V_lower','image',0,255,nothing)

# create trackbars for Lower HSV


cap = cv2.VideoCapture(0)

while(True):
    
    #Read frames from the camera
    _,frame = cap.read()
    
    # get current positions of four trackbars
    h_upper = cv2.getTrackbarPos('H_upper','image')
    s_upper = cv2.getTrackbarPos('S_upper','image')
    v_upper = cv2.getTrackbarPos('V_upper','image')
    
    h_lower = cv2.getTrackbarPos('H_lower','image')
    s_lower = cv2.getTrackbarPos('S_lower','image')
    v_lower = cv2.getTrackbarPos('V_lower','image')
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color = np.array([h_lower,s_lower,v_lower])                 #select range of HSV values      
    upper_color = np.array([h_upper,s_upper,v_upper])
    mask = cv2.inRange(hsv, lower_color, upper_color)   #mask the selected colour

    kernel = np.ones((3,3),np.uint8)                           
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)     #Morphological transformation (opening) to reduce noise

    cv2.imshow('Result',opening)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
