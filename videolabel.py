from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from PIL import Image

import screenshot

class VideoThread(QtCore.QThread):
    frameFinished = QtCore.pyqtSignal('PyQt_PyObject')

    def __init__(self, screen_to_capture, parent=None):
        super(VideoThread, self).__init__(parent)
        
        self.screen_to_capture = screen_to_capture

    def run(self):
        while True:
            image = screenshot.get_mirrored_screenshot(self.screen_to_capture)
            pixmap = screenshot.pil_to_qpixmap(image)

            self.frameFinished.emit(pixmap)

class VideoLabel(QtWidgets.QLabel):
    def __init__(self, screen_to_capture, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

        self.setWindowTitle("screen mirror")

        self.thread = VideoThread(screen_to_capture)
        self.thread.frameFinished.connect(self.frameFinished)
        self.thread.finished.connect(self.close)
        self.thread.start()

    def frameFinished(self, pixmap):
        self.setGeometry(200, 200, pixmap.size().width(), pixmap.size().height())
        self.setPixmap(pixmap)
       