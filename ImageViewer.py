

from widget import Widget
import sys
from PySide6.QtWidgets import QApplication


class ImageViewer(Widget):
    def __init__(self,):
        super().__init__()

    


    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageViewer()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
