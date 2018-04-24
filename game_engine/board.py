import cv2


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, frame, ratio, x_shift, y_shift):
        top_left = (int(x_shift), int(y_shift))
        bottom_right = (int(self.width * ratio + x_shift), int(self.height * ratio + y_shift))
        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 0), -1)
