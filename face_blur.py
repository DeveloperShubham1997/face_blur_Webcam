import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    
  
    face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img) 
    
    for (x,y,w,h) in face_rects: 
        #cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
        ROI=face_img[y:y+h, x:x+w]
        #blur = cv2.GaussianBlur(ROI, (71,71), 0) 
        
        fw, fh = (8, 8)

        # Resize input to "pixelated" size
        temp = cv2.resize(ROI, (fw, fh), interpolation=cv2.INTER_LINEAR)

        # Initialize output image
        output = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
        
        face_img[y:y+h, x:x+w] = output
        #drawshape(face_img,x,y,w,h)
        
    return face_img


cap = cv2.VideoCapture(0) 

while True: 
    
    ret, frame = cap.read(0) 
     
    frame = detect_face(frame)
 
    cv2.imshow('Video Face Detection', frame) 
 
    c = cv2.waitKey(1) 
    if c == 27: 
        break 
        
cap.release() 
cv2.destroyAllWindows()
