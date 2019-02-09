from PIL import Image
from mss import mss

from PyQt5 import QtGui


def get_mirrored_screenshot(screen_to_capture):
    with mss() as screenshot:
        raw_image = screenshot.grab(screenshot.monitors[screen_to_capture])
        pil_image = Image.frombytes("RGB", raw_image.size, raw_image.bgra, "raw", "BGRX")

        pil_image = pil_image.transpose(Image.FLIP_LEFT_RIGHT)

        return pil_image

def pil_to_qpixmap(pil_image):
    w, h = pil_image.size
    data = pil_image.tobytes("raw", "BGRX")
    qimage = QtGui.QImage(data, w, h, QtGui.QImage.Format_RGB32)
    pix = QtGui.QPixmap.fromImage(qimage)
    return pix