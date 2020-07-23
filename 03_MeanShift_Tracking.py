import cv2
import numpy as np

# capture video input
cap = cv2.VideoCapture('Video/face_track.mp4')

# take first frame of the video
ret, frame = cap.read()

# set up the tracking window
face_casc = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
face_rects = face_casc.detectMultiScale(frame)

# convert a list to tuple
face_x, face_y, w, h = tuple(face_rects[0])
track_window = (face_x, face_y, w, h)

# set up the ROI for tracking
roi = frame[face_y:face_y+h, face_x:face_x+w]

# HSV color mapping
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# histogram to target on each frame for the meanshift calculation
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0,180])

# normalize the histogram
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# set the termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# while loop
while True:
    # capture video
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # calculate the base of ROI
        dest_roi = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        # meanshift to get the coordinates of the rectangle
        ret, track_window = cv2.meanShift(dest_roi,
                                          track_window,
                                          term_crit)
        # draw new rectangle on image
        x, y, w, h = track_window

        # open new window or display
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255, 0), 3)
        cv2.imshow('FaceTracker', img2)

        # close window
        if cv2.waitKey(50) & 0xFF == 27:
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()


