import cv2

class Annotations:
    def __init__(self):
        self.annotations = [[]]
        self.annotation_number = -1
        self.annotation_start = False

    def add_annotation(self, indexFinger):
        if not self.annotation_start:
            self.annotation_start = True
            self.annotation_number += 1
            self.annotations.append([])

        self.annotations[self.annotation_number].append(indexFinger)

    def remove_last_annotation(self):
        if self.annotations:
            self.annotations.pop(-1)
            self.annotation_number -= 1

    def draw_annotations(self, slide):
        for annotation in self.annotations:
            for j in range(len(annotation)):
                if j != 0:
                    cv2.line(slide, annotation[j - 1], annotation[j], (0, 0, 200), 12)
    
    def reset_annotations(self):
        self.annotations = [[]]
        self.annotation_number = -1
        self.annotation_start = False        
