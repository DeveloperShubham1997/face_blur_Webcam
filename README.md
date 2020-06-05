# face_blur_Webcam
This is a jupyter notebook which contains a code to blur your face on live camera

To detect face haarcascade_frontalface_default classifier is used it return the bounding box around the face 

Bounding box is treated as region of intrest for blurring. ROI is reduced to very small size (16X16) [ you can play around the size and get diffrent blur] then again resized to orignal dimensions.

