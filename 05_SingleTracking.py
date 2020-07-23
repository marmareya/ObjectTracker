import cv2

# define our tracker API already exists
def ask_for_tracker():
    print('Hi !  What tracker API would you like to use?')
    print('Enter 0 for BOOSTING: ')
    print('Enter 1 for MIL: ')
    print('Enter 2 for KCF: ')
    print('Enter 3 for TLD: ')
    print('Enter 4 for MEDIANFLOW: ')
    print('Enter 5 for GOTURN: ')
    print('Enter 6 for MOSSE: ')
    print('Enter 7 for CSRT: ')

    choice = input('Please select your tracker: ')

    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
    if choice == '5':
        tracker = cv2.TrackerGOTURN_create()
    if choice == '6':
        tracker = cv2.TrackerMOSSE_create()
    if choice == '7':
        tracker = cv2.TrackerCSRT_create()

    return tracker

# tracker
tracker = ask_for_tracker()

# tracker name
tracker_name = str(tracker).split()[0][1:]

# capture the video
cap = cv2.VideoCapture('Video/Vehicles.mp4')

# read the 1st frame
ret, frame = cap.read()

# select out ROI
roi = cv2.selectROI(frame, False)

# initialize tracker
ret = tracker.init(frame, roi)

# While loop
while True:
    ret, frame = cap.read()

    # update tracker
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))

    # draw rectangles as tracker moves
    if success:
        # Success on tracking
        pts1 = (x, y)
        pts2 = (x+w, y+h)
        cv2.rectangle(frame, pts1, pts2,
                      (255,125,25), 3)

    else:
        #failure of tracking
        cv2.putText(frame,
                    'Failed to track the object',
                    (100, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (25,125.255), 3)

    # Display tracker
    cv2.putText(frame,
                tracker_name,
                (20, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255,255,0), 3)

    # Display result
    cv2.imshow(tracker_name, frame)

    # exit with Esc button
    if cv2.waitKey(50) & 0xFF == 27:
        break


# release the capture & destroy all windows
cap.release()
cv2.destroyAllWindows()




