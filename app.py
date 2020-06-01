import cv2

from src.Capturer import Capturer

if __name__ == "__main__":
    c = Capturer(save_frequency=5)
    while True:
        _, frame = c.capture()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
