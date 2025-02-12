import cv2
from config import WIDTH, HEIGHT, SLIDE_CHANGE_DELAY
from hand_tracking import HandTracking
from slide_controller import SlideController
from annotations import Annotations
from config import WIDTH, HEIGHT, GESTURE_THRESHOLD_Y, GESTURE_THRESHOLD_X


print("Presentation Has Begun....")

# Initialize HandTracking, SlideController, and Annotations
hand_tracking = HandTracking()
slide_controller = SlideController()
annotations = Annotations()

# Camera Setup
video_capture = cv2.VideoCapture(0)
video_capture.set(3, WIDTH)
video_capture.set(4, HEIGHT)

# Variables
is_button_pressed = False
counter = 0
user_video_height, user_video_width = int(197 * 1), int(350 * 1)  # width and height of small image
while True:
    # Get image frame
    success, video_frame = video_capture.read()
    video_frame = cv2.flip(video_frame, 1)

    # Load current slide
    current_slide = slide_controller.load_slide()

    # Find the hand and its landmarks
    hands, video_frame = hand_tracking.detect_hand(video_frame)
    
    # Draw Gesture Threshold line
    cv2.line(video_frame, (GESTURE_THRESHOLD_X, GESTURE_THRESHOLD_Y), (WIDTH, GESTURE_THRESHOLD_Y), (255, 0, 0), 10)
    cv2.line(video_frame, (GESTURE_THRESHOLD_X, 0), (GESTURE_THRESHOLD_X, GESTURE_THRESHOLD_Y), (255, 0, 0), 10)

    if hands and not is_button_pressed:  # If hand is detected
        hand = hands[0]
        cx, cy = hand["center"]
        xVal, yVal = hand_tracking.get_finger_position(hand)
        indexFinger = xVal, yVal

        fingers = hand_tracking.hand_detector.fingersUp(hand)  # Get the fingers that are up

        if hand_tracking.is_gesture_in_region(cx, cy):  # If hand is at the height of the face
            if fingers == [1, 0, 0, 0, 0]:  # Left gesture
                print("Left")
                is_button_pressed = True
                slide_controller.previous_slide()
                annotations.reset_annotations()
            elif fingers == [1, 1, 0, 0, 0]:  # Right gesture
                print("Right")
                is_button_pressed = True
                slide_controller.next_slide()
                annotations.reset_annotations()

        if fingers == [0, 1, 0, 0, 0]:  # Annotation gesture
            cv2.circle(current_slide, indexFinger, 12, (0, 179, 179), cv2.FILLED)

        if fingers == [0, 1, 1, 0, 0]:  # Add annotation
            annotations.add_annotation(indexFinger)
            cv2.circle(current_slide, indexFinger, 12, (0, 0, 255), cv2.FILLED)
        
        elif fingers == [0, 1, 1, 1, 0]:  # Remove annotation
            annotations.remove_last_annotation()
            is_button_pressed = True

    else:
        annotations.annotation_start = False

    if is_button_pressed:
        counter += 1
        if counter > SLIDE_CHANGE_DELAY:
            counter = 0
            is_button_pressed = False

    # Draw annotations on slide
    annotations.draw_annotations(current_slide)

    # Overlay video on slide
    user_video = cv2.resize(video_frame, (user_video_width, user_video_height))
    current_slide_height, current_slide_width, _ = current_slide.shape
    current_slide[current_slide_height - user_video_height:current_slide_height, current_slide_width - user_video_width: current_slide_width] = user_video

    # Show the image
    cv2.imshow("Slides", current_slide)
    # cv2.imshow("Image", video_frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
