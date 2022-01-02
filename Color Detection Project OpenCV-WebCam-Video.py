# Color Detection Using web Cam

#Importing OpenCV and Numpy
import cv2
import numpy as np

#Setting the Frame Width
frameWidth = 640
#Setting the Frame Height
frameHeight = 480
#Command to Take the input from web cam ( we can use external camera by putting 1 in the bracket )
vid = cv2.VideoCapture(0)
#Setting the Width and Height for the video frame
vid.set(3,frameWidth)
vid.set(3,frameHeight)
# Setting the Brightness as 150 you change accordingly
vid.set(10,150)

#Defining a Empty function
def empty(a):
    pass

#Making the Hue,Saturation,Value adjustments for the captured image or frame
cv2.namedWindow("TrackBars")
#Setting up the window size
cv2.resizeWindow("TrackBars",640,240)
#Setting up the range for Hue,Saturation,Value
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",0,179,empty)
cv2.createTrackbar("Saturation Min","TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",0,255,empty)
cv2.createTrackbar("Value Min","TrackBars",0,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
    # Check is the variable to check the boolean value and frame is variable to read frames of video
    check,frame = vid.read()
    # Converting the captured frames from BGR to HSV
    vidHsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max","TrackBars")
    v_min = cv2.getTrackbarPos("Value Min","TrackBars")
    v_max = cv2.getTrackbarPos("Value Max","TrackBars")
    print(h_min)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(vidHsv,lower,upper)
    # Putting the Resulted Image in the same color as of the original image
    # To Change the Resulted Image color you can put BGR Values at the place of frames before mask!
    vidResult = cv2.bitwise_and(frame,frame,mask=mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    # For Showing the Original Frame
    cv2.imshow("Original",frame)
    # For Showing the HSV Frame
    cv2.imshow("HSV",vidHsv)
    # For Showing the Mask Frame
    cv2.imshow("Mask",mask)
    # For Showing the Result Frame
    cv2.imshow("Resulted image", vidResult)
    # setting the program exit button as q
    if cv2.waitKey(1) & 0XFF == ord("q"):
            break
#Finishing Commands
vid.release()
cv2.destroyAllWindows()