import os
import time

import cv2


def merge(path, fps=30):
    images = [img for img in sorted(os.listdir(path)) if img.endswith(".jpg")]
    video_name = time.strftime("%m-%d-%Y_%H%M%S", time.localtime()) + '.mp4'
    frame = cv2.imread(os.path.join(path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))

    cv2.destroyAllWindows()
    video.release()
