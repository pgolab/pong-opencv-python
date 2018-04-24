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

        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#contours-getting-started
        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features
        # max(contours, key=cv2.contourArea)

        return position, fingers_count

    def _get_interesting_pixels_mask(self, frame):
        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering
        # http://docs.opencv.org/3.1.0/db/d5c/tutorial_py_bg_subtraction.html
        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding

        return None

    @staticmethod
    def _get_transformed_pixels_mask(mask):
        # http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
        # http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_filtering/py_filtering.html#filtering

        return None

    @staticmethod
    def _get_fingers_count(hand_contour):
        # https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
        # https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html
        # https://en.wikipedia.org/wiki/Law_of_cosines

        return 0


