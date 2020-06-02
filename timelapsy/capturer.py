import os

import cv2
import time


class Capturer:
    def __init__(
        self,
        address: str,
        save_frequency: int,
        save_path: str,
    ):
        """
        Capturer class is responsible for capturing frames from a provided address
        :param address: The address from which to capture video feed
        :param save_frequency: Frequency (in seconds) to save image to disk
        :param save_path: Where to store saved images
        """
        self._capture = cv2.VideoCapture(str(address))
        self._last_capture = save_frequency

        self.save_frequency = max(
            save_frequency, 1
        )  # If less than 1second just record a video

        self.save_path = save_path
        if not os.path.exists(save_path):
            os.mkdir(save_path)

    def capture(self):
        """
        Captures the frame from the specific video feed
        :return: the captured frame
        """
        ret, frame = self._capture.read()
        now = time.time()
        if now - self._last_capture >= self.save_frequency and ret:
            self._last_capture = now
            self._save_frame(frame)

        return frame

    def _save_frame(self, frame):
        """
        Saves the captured frame to disk
        :param frame: The frame to save to disk
        :return:
        """
        if frame is None:
            return

        cv2.imwrite(
            os.path.join(
                self.save_path,
                time.strftime("%m-%d-%Y_%H%M%S", time.localtime()) + ".jpg",
            ),
            frame,
        )
