import cv2
import sys
from random import randint


# tracker types
tracker_types = ['BOOSTING',
                 'MIL',
                 'KCF',
                 'TLD',
                 'MEDIANFLOW',
                 'GOTURN',
                 'MOSSE',
                 'CSRT']

# define trackers by name
def tracker_name(tracker_types):
    # create trackers by name
    if tracker_types == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif tracker_types == tracker_types[2]:
        tracker = cv2.TrackerKFC_create()
    elif tracker_types == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()
    elif tracker_types == tracker_types[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_types == tracker_types[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif tracker_types == tracker_types[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif tracker_types == tracker_types[7]:
        tracker = cv2.TrackerCSRT_create()

    # else statement
    else:
        tracker = None
        print('No tracker found')
        print('Choose from these trackers: ')
        for tr in tracker_types:
            print(tr)

    return tracker

if __name__ == '__main__':
    print('Default tracking algorithm MOSSE \n'
          'Available algorithms are: \n')
    for tr in tracker_types:
        print(tr)

    trackerType = 'MOSSE'

    # Create a video capture
    cap = cv2.VideoCapture('Video/Vehicles.mp4')

    # read first frame
    success, frame = cap.read()

    # Quit if failure
    if not success:
        print('Cannot read the video')

    # Select boxes and colors
    rects = []
    colors = []

    # While loop
    while True:
        # draw rectangles, select ROI, open new window
        rect_box = cv2.selectROI('MultiTracker', frame)
        rects.append(rect_box)
        colors.append((randint(64,255), randint(64,255), randint(64,255)))
        print('Press Q to stop selecting boxes and start multitracking')
        print('Press any key to select another box')

        # close window
        if cv2.waitKey(0) & 0xFF == 113:
            break

    # print message
    print("Selected boxes {}".format(rects))

    # Create multi tracker
    multitracker = cv2.MultiTracker_create()

    # initialize multitracker
    for rect_box in rects:
        multitracker.add(tracker_name(tracker_types),
                         frame,
                         rect_box)

    # Video and Tracker
    # while loop
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # update location objects
        success, boxes = multitracker.update(frame)

        # draw the objects tracked
        for i, newbox in enumerate(boxes):
            pts1 = (int(newbox[0]),
                    int(newbox[1]))
            pts2 = (int(newbox[0] + newbox[2]),
                    int(newbox[1] + newbox[3]))
            cv2.rectangle(frame,
                          pts1,
                          pts2,
                          colors[i],
                          2,
                          1)

        # display frame
        cv2.imshow('Multitracker', frame)

        # close the frame
        if cv2.waitKey(20) & 0xFF == 27:
            break

# release and destroy
cap.release()
cv2.destroyAllWindows()




