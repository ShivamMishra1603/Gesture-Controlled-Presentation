import os
import cv2
from config import FOLDER_PATH

class SlideController:
    def __init__(self):
        self.current_slide_number = 0
        self.list_of_slides = sorted(os.listdir(FOLDER_PATH), key=len)
        print(self.list_of_slides)

    def load_slide(self):
        slide_path = os.path.join(FOLDER_PATH, self.list_of_slides[self.current_slide_number])
        return cv2.imread(slide_path)

    def next_slide(self):
        if self.current_slide_number < len(self.list_of_slides) - 1:
            self.current_slide_number += 1

    def previous_slide(self):
        if self.current_slide_number > 0:
            self.current_slide_number -= 1
