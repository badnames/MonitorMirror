from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PIL import Image

import screenshot

class ImageLabel(QtWidgets.QLabel):
    def __init__(self, pil_image, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

        self.setGeometry(200, 200, pil_image.size[0], pil_image.size[1])
        self.setWindowTitle("screen mirror")

        pixmap = screenshot.pil_to_qpixmap(pil_image)
        self.setPixmap(pixmap)
