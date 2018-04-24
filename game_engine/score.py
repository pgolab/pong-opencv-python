import cv2

NUMBERS_DISPLAY = {
    0: [[True, True, True], [True, False, True], [True, False, True], [True, False, True], [True, True, True]],
    1: [[False, True, False], [False, True, False], [False, True, False], [False, True, False], [False, True, False]],
    2: [[True, True, True], [False, False, True], [True, True, True], [True, False, False], [True, True, True]],
    3: [[True, True, True], [False, False, True], [True, True, True], [False, False, True], [True, True, True]],
    4: [[True, False, True], [True, False, True], [True, True, True], [False, False, True], [False, False, True]],
    5: [[True, True, True], [True, False, False], [True, True, True], [False, False, True], [True, True, True]],
    6: [[True, True, True], [True, False, False], [True, True, True], [True, False, True], [True, True, True]],
    7: [[True, True, True], [False, False, True], [False, False, True], [False, False, True], [False, False, True]],
    8: [[True, True, True], [True, False, True], [True, True, True], [True, False, True], [True, True, True]],
    9: [[True, True, True], [True, False, True], [True, True, True], [False, False, True], [True, True, True]]
}


class Score:
    MAX_SCORE = 9

    def __init__(self, a_score_center, b_score_center):
        self.a_score = 0
        self.b_score = 0

        self.a_score_center = a_score_center
        self.b_score_center = b_score_center

    def reset(self):
        self.a_score = 0
        self.b_score = 0

    def a_scored(self):
        self.a_score += 1

    def b_scored(self):
        self.b_score += 1

    def draw(self, frame, ratio, x_shift, y_shift):
        self.draw_score(self.a_score, self.a_score_center, frame, ratio, x_shift, y_shift)
        self.draw_score(self.b_score, self.b_score_center, frame, ratio, x_shift, y_shift)

    def draw_score(self, score, score_center, frame, ratio, x_shift, y_shift):
        cx, cy = score_center

        for x in range(0, 3):
            for y in range(0, 5):
                if NUMBERS_DISPLAY[score][y][x]:
                    self.draw_pixel((cx + x - 1, cy + y - 2), frame, ratio, x_shift, y_shift)

    @staticmethod
    def draw_pixel(position, frame, ratio, x_shift, y_shift):
        x, y = position
        top_left = (int(x * ratio + x_shift), int(y * ratio + y_shift))
        bottom_right = (int((x + 1) * ratio + x_shift), int((y + 1) * ratio + y_shift))
        cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), -1)
