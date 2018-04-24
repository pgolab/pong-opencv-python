import cv2
import math

from config import BOARD_WIDTH, BOARD_HEIGHT, PADDLE_HEIGHT
from game_engine.ball import Ball
from game_engine.board import Board
from game_engine.paddle import Paddle
from game_engine.score import Score


class PongGame:
    def __init__(self):
        self.board = None
        self.paddle_a = None
        self.paddle_b = None
        self.ball = None
        self.score = None

        self.reset_game()

    def reset_game(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)

        self.paddle_a = Paddle(0, BOARD_HEIGHT / 2 - math.ceil(PADDLE_HEIGHT / 2), 1,
                               BOARD_HEIGHT / 2 + math.floor(PADDLE_HEIGHT / 2))
        self.paddle_b = Paddle(BOARD_WIDTH - 1, BOARD_HEIGHT / 2 - math.ceil(PADDLE_HEIGHT / 2), BOARD_WIDTH,
                               BOARD_HEIGHT / 2 + math.floor(PADDLE_HEIGHT / 2))

        self.ball = Ball(BOARD_WIDTH / 2, BOARD_HEIGHT / 2)

        self.score = Score((BOARD_WIDTH / 4, BOARD_HEIGHT / 8), (BOARD_WIDTH / 4 * 3, BOARD_HEIGHT / 8))

    def make_move(self, user_target_y=None, frame_height=0):
        if self.score.a_score == Score.MAX_SCORE or self.score.b_score == Score.MAX_SCORE:
            return

        ball = self.ball
        board = self.board
        paddle_a = self.paddle_a
        paddle_b = self.paddle_b

        ball.make_move()

        if (ball.y == 0) or (ball.y == board.height - 1):
            ball.v_y *= -1

        a_scored = ball.x == board.width
        b_scored = ball.x == -1

        if a_scored:
            self.score.a_scored()

        if b_scored:
            self.score.b_scored()

        if a_scored or b_scored:
            ball.x = board.width / 2
            ball.y = board.height / 2
            ball.v_x *= -1

        paddle_a.make_ai_move(board, ball)

        if user_target_y is None:
            paddle_b.make_ai_move(board, ball)
        else:
            height_ratio = math.floor(frame_height / board.height)
            user_target_y = max(int(user_target_y / height_ratio), 0)
            paddle_b.make_move_towards(board, user_target_y)

        a_collides = paddle_a.collides_with_ball(ball)
        b_collides = paddle_b.collides_with_ball(ball)
        if a_collides or b_collides:
            ball.v_x *= -1

    def draw(self, frame):
        ball = self.ball
        board = self.board
        paddle_a = self.paddle_a
        paddle_b = self.paddle_b
        score = self.score

        (frameHeight, frameWidth, _) = frame.shape

        width_ratio = math.floor(frameWidth / board.width)
        height_ratio = math.floor(frameHeight / board.height)
        ratio = min(width_ratio, height_ratio)
        x_shift = (frameWidth - board.width * ratio) / 2
        y_shift = (frameHeight - board.height * ratio) / 2

        frame_clone = frame.copy()
        board.draw(frame_clone, ratio, x_shift, y_shift)

        cv2.addWeighted(frame, 0.3, frame_clone, 0.7, 0.0, frame)

        paddle_a.draw(frame, ratio, x_shift, y_shift)
        paddle_b.draw(frame, ratio, x_shift, y_shift)
        ball.draw(frame, ratio, x_shift, y_shift)

        score.draw(frame, ratio, x_shift, y_shift)
