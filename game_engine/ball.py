import cv2


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.v_x = 1
        self.v_y = 1

    def make_move(self):
        self.x += self.v_x
        self.y += self.v_y

    def draw(self, frame, ratio, x_shift, y_shift):
        top_left = (int(self.x * ratio + x_shift), int(self.y * ratio + y_shift))
        bottom_right = (int((self.x + 1) * ratio + x_shift), int((self.y + 1) * ratio + y_shift))
        cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), -1)
