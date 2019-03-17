import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    
    #Read frames from the camera
    _,frame = cap.read()
    
    #Split the color channels
    b,g,r = cv2.split(frame)
    
    #Equalise each color channel
    b_equ = cv2.equalizeHist(b)
    g_equ = cv2.equalizeHist(g)
    r_equ = cv2.equalizeHist(r)
    
    #Merge the color channels
    equ = cv2.merge((b_equ,g_equ,r_equ))

    #Stack the images side-by-side
    res = np.hstack((frame,equ))
    
    #Display the image
    cv2.imshow('Result',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()





 

