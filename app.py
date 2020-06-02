from typing import Any

import click
import cv2

from timelapsy.capturer import Capturer
from timelapsy.merge import merge


@click.command()
@click.option(
    "--address",
    default="0",
    help="Address of stream, can also be webcam device id (e.g: http://192.168.1.166:8080/video) for ip camera"
)
@click.option("--save-frequency", default=300, help="Saves frame/image every X seconds")
@click.option("--save-path", default='images', help="Directory where to store files")
def capture(address, save_frequency, save_path):
    c = Capturer(address=address, save_frequency=save_frequency, save_path=save_path)
    while True:
        frame = c.capture()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    merge(c.save_path)


if __name__ == "__main__":
    capture()
