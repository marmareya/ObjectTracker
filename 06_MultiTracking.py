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
    cap = cv2.VideoCapture('Video/Vahicles.mp4')

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
    print(f'Selected boxes {rects}')

    # Create multi tracker
    multitracker = cv2.




