# Color Detection Using Image


#Importing OpenCV and Numpy
import cv2
import numpy as np

#Defining a Empty function
def empty(a):
    pass
#Making the Hue,Saturation,Value adjustments for the captured image or frame
cv2.namedWindow("TrackBars")
#Setting up the window size
cv2.resizeWindow("TrackBars",640,240)
#Setting up the range for Hue,Saturation,Value
cv2.createTrackbar("Hue Min","TrackBars",32,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",87,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",34,255,empty)
cv2.createTrackbar("Value Min","TrackBars",71,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
    # Reading the image using imread
    img = cv2.imread("box.jpg")
    # Converting the captured image from BGR to HSV
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBars")
    v_min = cv2.getTrackbarPos("Value Min","TrackBars")
    v_max = cv2.getTrackbarPos("Value Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    # Putting the Resulted Image in the blue color
    # To Change the Resulted Image color you can put img at the place of the BGR value before mask!
    imgResult = cv2.bitwise_and(img,(255,0,0),mask=mask)

    # For Showing the Original Frame
    cv2.imshow("Original",img)
    # For Showing the HSV Frame
    cv2.imshow("HSV",imghsv)
    # For Showing the Mask Frame
    cv2.imshow("Mask",mask)
    # For Showing the Result Frame
    cv2.imshow("Resulted image", imgResult)
    #Putting the waitkey to hold the frame so that we can see the image
    cv2.waitKey(1)



