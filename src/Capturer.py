import os

import cv2
import time


class Capturer:
    def __init__(
        self,
        address: str = "http://192.168.1.166:8080/video",
        save_frequency: int = 600,
        save_path: str = "images",
    ):
        self._capture = cv2.VideoCapture(address)
        self.save_frequency = max(
            save_frequency, 1
        )  # If less than 1second just record a video
        self._last_capture = save_frequency
        self.save_path = save_path

    def capture(self):
        ret, frame = self._capture.read()
        now = time.time()
        if now - self._last_capture >= self.save_frequency and ret:
            self._last_capture = now
            self._save_frame(frame)

        return ret, frame

    def _save_frame(self, frame):
        if frame is None:
            return

        cv2.imwrite(
            os.path.join(
                self.save_path,
                time.strftime("%b-%d-%Y_%H%M%S", time.localtime()) + ".jpg",
            ),
            frame,
        )
