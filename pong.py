import imutils
import cv2

from config import SHOW_DETECTIONS
from detector.hand_detector import HandDetector
from game_engine.pong_game import PongGame
from utils.kalman import KalmanTracker
from utils.positions_display import PositionsDisplay


def run_game(display_detections=False, input_path=None):
    if input_path is None:
        video_capture = cv2.VideoCapture(0)
    else:
        video_capture = cv2.VideoCapture(input_path)

    position = (0, 0)

    pong_game = PongGame()

    hand_detector = HandDetector()

    kalman_tracker = KalmanTracker()
    if display_detections:
        positions_display = PositionsDisplay()

    while True:
        (grabbed, frame) = video_capture.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=1000)
        frame = cv2.flip(frame, 1)

        new_position, fingers_count = hand_detector.get_hand_position(frame)
        if new_position is not None:
            position = new_position

            if fingers_count == 5:
                pong_game.reset_game()

        kalman_tracker.add_measurement(position)
        kalman_prediction = kalman_tracker.get_prediction()

        if display_detections:
            positions_display.track(position, kalman_prediction)
            positions_display.draw(frame)

        pong_game.make_move(kalman_prediction[1], frame.shape[0])
        pong_game.draw(frame)

        cv2.imshow("result", frame)

        key = cv2.waitKey(100) & 0xFF
        if key == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_game(SHOW_DETECTIONS)
