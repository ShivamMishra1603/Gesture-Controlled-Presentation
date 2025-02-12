from cvzone.HandTrackingModule import HandDetector
import numpy as np
from config import HAND_DETECTION_CONFIDENCE, MAX_HANDS, WIDTH, HEIGHT, GESTURE_THRESHOLD_Y, GESTURE_THRESHOLD_X

class HandTracking:
    def __init__(self):
        self.hand_detector = HandDetector(detectionCon=HAND_DETECTION_CONFIDENCE, maxHands=MAX_HANDS)

    def detect_hand(self, frame):
        hands, frame = self.hand_detector.findHands(frame)  # with draw
        return hands, frame

    def get_finger_position(self, hand):
        lmList = hand["lmList"]
        xVal = int(np.interp(lmList[8][0], [WIDTH // 2, WIDTH], [0, WIDTH + 1100]))
        yVal = int(np.interp(lmList[8][1], [150, HEIGHT - 150], [0, HEIGHT + 500]))
        return xVal, yVal

    def is_gesture_in_region(self, cx, cy):
        return cy <= GESTURE_THRESHOLD_Y and cx >= GESTURE_THRESHOLD_X
