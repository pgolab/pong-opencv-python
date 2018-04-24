import cv2
import numpy as np


class KalmanTracker:
    def __init__(self):
        self.measurement = np.array((2, 1), np.float32)
        self.prediction = np.zeros((2, 1), np.float32)

        self.kalman = cv2.KalmanFilter(4, 2)
        self.kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
        self.kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
        self.kalman.processNoiseCov = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.03

    def add_measurement(self, new_measurement):
        self.measurement = np.array([[np.float32(new_measurement[0])], [np.float32(new_measurement[1])]])

    def get_prediction(self):
        self.kalman.correct(self.measurement)
        prediction = self.kalman.predict()
        return int(prediction[0]), int(prediction[1])
