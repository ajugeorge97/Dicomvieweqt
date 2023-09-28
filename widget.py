# This Python file uses the following encoding: utf-8
import sys
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout,QSizePolicy

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from pydicom import dcmread


import sys

import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import SimpleITK as sitk




class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        
        self.ui.setupUi(self)
        self.handle_image_viewer(self.ui.viewer)
        self.showMaximized()            
        self.initUI()

    def handle_dicom(self,path):

        return dcmread(path)


    def handle_image_viewer(self,viewer):
        viewer.setStyleSheet("background-color:#808080;")

        self.QHBoxLayout_viewer=QHBoxLayout(viewer)
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)
        self.image_viewer=FigureCanvas(Figure(figsize=(10, 3),facecolor='black'))
        # Ideally one would use self.addToolBar here, but it is slightly
        # incompatible between PyQt6 and other bindings, so we just add the
        # toolbar as a plain widget instead.
        #self.QHBoxLayout_viewer.addWidget(NavigationToolbar(self.image_viewer, self))
        self.QHBoxLayout_viewer.addWidget(self.image_viewer)
        tbar=NavigationToolbar(self.image_viewer)
        tbar.pan()

        self._static_ax = self.image_viewer.figure.subplots()
        t = np.linspace(0, 10, 501)
        data=self.handle_dicom(path="Dicomvieweqt/Sampledata/series-000001/image-000001.dcm")
        self._static_ax.imshow(data.pixel_array, cmap=plt.cm.gray)
        self._static_ax.axis('off')


        #sizepolicy=QSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
        #sizepolicy.setHorizontalPolicy(QSizePolicy.Maximum)
        #sizepolicy.setVerticalPolicy(QSizePolicy.Maximum)
        #sizepolicy.setHorizontalStretch(0)
        #sizepolicy.setVerticalStretch(0)
        #sizepolicy.setHeightForWidth(self.image_viewer.sizePolicy().hasHeightForWidth())
        #self.image_viewer.setSizePolicy(sizepolicy)

        #self.image_viewer.setScaledContents(True)
        #self.image_viewer.setFrameShape(QFrame.StyledPanel)
        #self.image_viewer.setFrameShadow(QFrame.Raised)
        self.image_viewer.setStyleSheet("background-color:#ffffff;")
        image=QPixmap("Dicomvieweqt/Screenshot 2023-09-28 at 11.58.11.png")
        #self.image_viewer.setPixmap(image)


    def initUI(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
