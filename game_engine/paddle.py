from random import random

import cv2

from config import USE_OPTIMAL_AI


class Paddle:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self._ai_direction = 0

    def collides_with_ball(self, ball):
        x_collides = (ball.x + 1 == self.left) or (ball.x == self.right)
        y_collides = (ball.y >= self.top) and (ball.y < self.bottom)
        return x_collides and y_collides

    def make_ai_move(self, board, ball):
        follow_ball = ((self.left < ball.x / 2) and (ball.v_x < 0)) \
                      or ((self.left > ball.x / 2) and (ball.v_x > 0))

        if not USE_OPTIMAL_AI and random() < 0.25:
            follow_ball = False

        if follow_ball:
            self.make_move_towards(board, ball.y)
        else:
            if USE_OPTIMAL_AI:
                self.make_move_towards(board, board.height / 2)
            else:
                direction_change = 0

                if random() < 0.5:
                    if self._ai_direction == 0:
                        direction_change = 1 if random() < 0.5 else -1
                    else:
                        direction_change = -self._ai_direction

                self._ai_direction += direction_change

                self.make_move(board, self._ai_direction)

    def make_move_towards(self, board, target_y):
        y_middle = (self.top + self.bottom) / 2

        if target_y > y_middle:
            velocity = 1
        elif target_y < y_middle:
            velocity = -1
        else:
            velocity = 0

        self.make_move(board, velocity)

    def make_move(self, board, y_diff):
        if self.top + y_diff < 0:
            return

        if self.bottom + y_diff > board.height:
            return

        self.top += y_diff
        self.bottom += y_diff

    def draw(self, frame, ratio, x_shift, y_shift):
        top_left = (int(self.left * ratio + x_shift), int(self.top * ratio + y_shift))
        bottom_right = (int(self.right * ratio + x_shift), int(self.bottom * ratio + y_shift))
        cv2.rectangle(frame, top_left, bottom_right, (255, 255, 255), -1)
