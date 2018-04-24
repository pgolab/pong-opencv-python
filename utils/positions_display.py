from collections import deque
import cv2
import numpy as np

from config import TRACKED_POSITIONS_COUNT


class PositionsDisplay:
    def __init__(self):
        self.tracked_positions = deque(maxlen=TRACKED_POSITIONS_COUNT)
        self.tracked_predictions = deque(maxlen=TRACKED_POSITIONS_COUNT)

    def track(self, position, prediction):
        self.tracked_positions.appendleft(position)
        self.tracked_predictions.appendleft(prediction)

    def draw(self, frame):
        self._draw_track(frame, self.tracked_positions, (0, 0, 255))
        self._draw_track(frame, self.tracked_predictions, (0, 255, 0))

    @staticmethod
    def _draw_track(frame, positions, color):
        for i in range(1, len(positions)):
            thickness = int(np.sqrt(TRACKED_POSITIONS_COUNT / float(i + 1)) * 2.5)
            cv2.line(frame, positions[i - 1], positions[i], color, thickness)

        cv2.circle(frame, positions[0], 10, color, -1)

