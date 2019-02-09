import sys

from mss import mss
from PIL import Image

from PyQt5 import QtWidgets

from imagelabel import ImageLabel
from videolabel import VideoLabel

import screenshot

if __name__ == "__main__":
    screen_to_capture = int(sys.argv[2])

    app = QtWidgets.QApplication(sys.argv)

    if sys.argv[1] == "-i":
        image = screenshot.get_mirrored_screenshot(screen_to_capture)
        imageLabel = ImageLabel(image)
        imageLabel.show()

    if sys.argv[1] == "-v":
        videoLabel = VideoLabel(screen_to_capture)
        videoLabel.show()        
    
    sys.exit(app.exec_())


