from math import ceil

import imutils
import cv2
import os

from config import PROJECT_ROOT


def record_video():
    video_capture = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    fps = 15.0

    output_path = PROJECT_ROOT / 'output.m4v';

    if output_path.exists():
        os.remove(output_path)

    out = cv2.VideoWriter(output_path.as_posix(), fourcc, fps, (1000, 562))

    while True:
        (grabbed, frame) = video_capture.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=1000)
        out.write(frame)
        frame = cv2.flip(frame, 1)

        cv2.imshow('capture', frame)

        key = cv2.waitKey(ceil(int(1000 / fps)))
        if key == ord('q'):
            break

    out.release()
    video_capture.release()


if __name__ == "__main__":
    record_video()
