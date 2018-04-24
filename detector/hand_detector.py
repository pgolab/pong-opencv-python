import cv2
from math import acos, pi
from config import SKIN_LOWER_BOUND, SKIN_UPPER_BOUND


class HandDetector:
    def __init__(self):
        self.fgbg = cv2.createBackgroundSubtractorMOG2()

    def get_hand_position(self, frame):
        position = None
        fingers_count = 0

        mask = self._get_interesting_pixels_mask(frame)
        transformed = self._get_transformed_pixels_mask(mask)

        contours = cv2.findContours(transformed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

        frame_clone = frame.copy()
        cv2.drawContours(frame_clone, contours, -1, (127, 127, 0), 2)

        if len(contours) > 0:
            max_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(max_contour)

            if radius > 10:
                position = (int(x), int(y) - int(radius) + 50)

            fingers_count = self._get_fingers_count(max_contour)

        if position is not None:
            cv2.drawContours(frame_clone, [max_contour], -1, (127, 0, 127), -1)

        cv2.imshow('contours', frame_clone)

        return position, fingers_count

    def _get_interesting_pixels_mask(self, frame):
        blur = cv2.blur(frame, (5, 5))

        fgmask = self._get_fg_mask(blur)
        skin_mask = self._get_skin_mask(blur)

        return cv2.addWeighted(fgmask, 0.5, skin_mask, 0.5, 0.0)

    def _get_fg_mask(self, frame):
        fgmask = self.fgbg.apply(frame)
        return cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)[1]

    @staticmethod
    def _get_skin_mask(frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        return cv2.inRange(hsv, SKIN_LOWER_BOUND, SKIN_UPPER_BOUND)

    @staticmethod
    def _get_transformed_pixels_mask(mask):
        thresholded = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)[1]

        big_ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        small_ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        dilation = cv2.dilate(thresholded, small_ellipse_kernel, iterations=1)
        erosion = cv2.erode(dilation, big_ellipse_kernel, iterations=2)
        dilation2 = cv2.dilate(erosion, big_ellipse_kernel, iterations=2)
        erosion2 = cv2.erode(dilation2, small_ellipse_kernel, iterations=1)

        return erosion2

    @staticmethod
    def _get_fingers_count(hand_contour):
        # https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
        # https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
        # https://en.wikipedia.org/wiki/Law_of_cosines

        return 0


