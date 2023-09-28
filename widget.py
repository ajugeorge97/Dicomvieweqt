# This Python file uses the following encoding: utf-8
import sys
import sys
from PySide6.QtGui import QPixmap,QPalette,QImage
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout,QSizePolicy

from OpenGL import GL as gl
from PySide6.QtWidgets import QApplication, QWidget

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QApplication, QFrame, QHBoxLayout, QLabel,QStackedLayout
from PySide6.QtCore import Qt
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget



class openGLviewer(QOpenGLWidget):
    def initializeGL(self):
            gl.glClearColor(0, 0, 0, 0)
    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        
        self.ui.setupUi(self)
        self.handle_image_viewer(self.ui.viewer)
        self.showMaximized()            
        self.initUI()

    def handle_image_viewer(self,viewer):
        viewer.setStyleSheet("background-color:#808080;")

        self.QHBoxLayout_viewer=QHBoxLayout(viewer)
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)
        self.image_viewer=QLabel() 

        sizepolicy=QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        sizepolicy.setHorizontalPolicy(QSizePolicy.Maximum)
        sizepolicy.setHorizontalStretch(0)
        sizepolicy.setVerticalStretch(0)
        #sizepolicy.setHeightForWidth(self.image_viewer.sizePolicy().hasHeightForWidth())
        self.image_viewer.setSizePolicy(sizepolicy)

        self.image_viewer.setScaledContents(True)
        self.image_viewer.setFrameShape(QFrame.StyledPanel)
        self.image_viewer.setFrameShadow(QFrame.Raised)
        self.QHBoxLayout_viewer.addWidget(self.image_viewer)
        self.image_viewer.setStyleSheet("background-color:#ffffff;")
        image=QPixmap("Dicomvieweqt/Screenshot 2023-09-28 at 11.58.11.png")
        self.image_viewer.setPixmap(image)


    def initUI(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
