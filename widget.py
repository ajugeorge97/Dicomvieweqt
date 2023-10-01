# This Python file uses the following encoding: utf-8
import sys
import sys
from PySide6.QtGui import QPixmap,QScrollEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout,QSizePolicy,QMainWindow
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from pydicom import dcmread
from pydicom.filereader import read_dicomdir


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
        self.showMaximized()
        self.setFixedSize(self.size())
        self.handle_image_viewer(self.ui.viewer)
        self.initUI()

    def handle_dicom(self,path,padding=True):
        if padding:
            return dcmread(path)
        
        
    def on_scroll(self, event):
        # Check if the event is a mouse scroll
        if event.inaxes is not None and event.button == 'up':
            # Zoom in
            #self.zoom(1.1)
            self.handle_image()
        elif event.inaxes is not None and event.button == 'down':
            # Zoom out
            #self.zoom(0.9)
            self.handle_image()
        #self.image_viewer.draw()
    def zoom(self, factor):
        xlim =self._static_ax.get_xlim()
        ylim =self._static_ax.axes.get_ylim()

        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2

        x_new = [x_center + (x - x_center) * factor for x in xlim]
        y_new = [y_center + (y - y_center) * factor for y in ylim]

        self._static_ax.set_xlim(x_new)
        self._static_ax.set_ylim(y_new)

    def wheelEvent(self, event):
        print(event.angleDelta().y())


    def handle_image(self,data):
        image_shape=data.pixel_array.shape[0]
        image_shape=data.pixel_array.shape[0]
        padding=int((self.aspect_ratio[0]*image_shape-image_shape)-(image_shape-self.aspect_ratio[1]*image_shape)/4)
        padded_array = np.pad(data.pixel_array, ((0,0), (padding,padding)), mode='constant', constant_values=0)
        self._static_ax = self.image_viewer.figure.subplots()
        self._static_ax.imshow(padded_array, cmap=plt.cm.gray)
        self._static_ax.axis('off')




    def handle_image_viewer(self,viewer):
        import os
        path=r"Sampledata/series-000001"
        data_set_path=[os.path.join(os.path.dirname(__file__),path,x) for x in os.listdir(path) if x.endswith('.dcm')]
        self.data=[self.handle_dicom(data) for data in data_set_path]
        image_shape=self.data[0].pixel_array.shape[0]

       

        self.QHBoxLayout_viewer=QHBoxLayout(viewer)
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)
        self.image_viewer=FigureCanvas(Figure(layout='tight',facecolor='black'))

        self.aspect_ratio=(self.image_viewer.geometry().width()/image_shape,self.image_viewer.geometry().height()/image_shape)

        self.QHBoxLayout_viewer.addWidget(self.image_viewer)
        tbar=NavigationToolbar(self.image_viewer)
        self.image_viewer.mpl_connect('scroll_event', self.on_scroll)
        tbar.pan()
        self.handle_image(self.data[0])



        # Pad the array



    def initUI(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
