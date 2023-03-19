# This Python file uses the following encoding: utf-8
import sys



from OpenGL import GL as gl
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
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
        self.showMaximized()
        openGLviewer().initializeGL()











if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
