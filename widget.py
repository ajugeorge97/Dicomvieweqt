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
        data=self.handle_dicom(path="Sampledata/series-000001/image-000001.dcm")

        self.QHBoxLayout_viewer=QHBoxLayout(viewer)
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)
        self.image_viewer=FigureCanvas(Figure(layout='tight',facecolor='black'))
        # Ideally one would use self.addToolBar here, but it is slightly

        # incompatible between PyQt6 and other bindings, so we just add the
        # toolbar as a plain widget instead.
        #self.QHBoxLayout_viewer.addWidget(NavigationToolbar(self.image_viewer, self))
        self.QHBoxLayout_viewer.addWidget(self.image_viewer)
        tbar=NavigationToolbar(self.image_viewer)
        tbar.pan()
        left_pad = 115
        right_pad = 115

        # Pad the array
        padded_array = np.pad(data.pixel_array, ((0, 0), (left_pad, right_pad)), mode='constant', constant_values=0)

        print(padded_array)

        self._static_ax = self.image_viewer.figure.subplots()
        self._static_ax.imshow(padded_array, cmap=plt.cm.gray,aspect=None)
        self._static_ax.axis('off')


    def initUI(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
