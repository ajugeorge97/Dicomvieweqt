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
import sys

from vtk_interaction import MyVtkInteractorStyleImage,StatusMessage
# noinspection PyUnresolvedReferences
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage
import vtkmodules.vtkRenderingContextOpenGL2
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
    vtkTextMapper,
    vtkTextProperty
    )

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        
        self.ui.setupUi(self)
        self.showMaximized()
        self.setFixedSize(self.size())
        self.handle_image_viewer(self.ui.viewer)
        self.initUI()

    def handle_image_viewer(self,viewer):
        folder=r"Sampledata/digest_article"
        colors=vtkNamedColors()
        reader=vtkDICOMImageReader()
        #Read DICOM files in the specified directory
        reader.SetDirectoryName(folder)
        reader.Update()
        

        self.QHBoxLayout_viewer=QHBoxLayout()
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)
        qvtk=QVTKRenderWindowInteractor(viewer)
        self.QHBoxLayout_viewer.addWidget(qvtk)
        viewer.setLayout(self.QHBoxLayout_viewer)

        #Visualilze
        image_viewer= vtkImageViewer2()
        image_viewer.SetRenderWindow(qvtk.GetRenderWindow())
        image_viewer.SetInputConnection(reader.GetOutputPort())
        #Slice status message 
        slice_text_prop=vtkTextProperty()
        slice_text_prop.SetFontFamilyToCourier()
        slice_text_prop.SetFontSize(20)
        slice_text_prop.SetVerticalJustificationToBottom()
        slice_text_prop.SetJustificationToLeft()
        #Slice status message
        slice_text_mapper=vtkTextMapper()
        msg=StatusMessage.format(image_viewer.GetSliceMin(),image_viewer.GetSliceMax())
        slice_text_mapper.SetInput(msg)
        slice_text_mapper.SetTextProperty(slice_text_prop)

        slice_text_actor=vtkActor2D()
        slice_text_actor.SetMapper(slice_text_mapper)
        slice_text_actor.SetPosition(15,10)

        #usage hint message 
        usage_text_prop=vtkTextProperty()
        usage_text_prop.SetFontFamilyToCourier()
        usage_text_prop.SetFontSize(14)
        usage_text_prop.SetVerticalJustificationToTop()
        usage_text_prop.SetJustificationToLeft()
        usage_text_mapper=vtkTextMapper()
        usage_text_mapper.SetInput(
            "Slice with mouse wheel\n  or Up/Down-Key\n- Zoom with pressed right\n "
            " mouse button while dragging"
        )
        usage_text_mapper.SetTextProperty(usage_text_prop)

        usage_text_actor=vtkActor2D ()
        usage_text_actor.SetMapper(usage_text_mapper)
        usage_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        usage_text_actor.GetPositionCoordinate().SetValue(0.05, 0.95)

        #Create an interactor with our own style (inherit from
        #vtkInteractorStyleImage in order to catch mousewheel and key events.
        #render_window_interactor= vtkRenderWindowInteractor()
        my_interactor_style=MyVtkInteractorStyleImage()
    
        #Make imageviewer2 and sliceTextMapper visible to our interactorstyle
        #to enable slice status message updates when  scrolling through the slices.
        my_interactor_style.set_imageviewer(image_viewer)
        my_interactor_style.set_status_mapper(slice_text_mapper)

        #Make the interactor use our own interactorstyle
        #cause SetupInteractor() is defining it's own default interatorstyle
        #this must be called after SetupInteractor().
        #renderWindowInteractor.SetInteractorStyle(myInteractorStyle);
        image_viewer.SetupInteractor(qvtk)
        qvtk.SetInteractorStyle(my_interactor_style)
        qvtk.Render()

        #Add slice status message and usage hint message to the renderer.
        image_viewer.GetRenderer().AddActor2D(slice_text_actor)
        image_viewer.GetRenderer().AddActor2D(usage_text_actor)

        # Initialize rendering and interaction.
        image_viewer.Render()
        image_viewer.GetRenderer().ResetCamera()
        image_viewer.GetRenderer().SetBackground(colors.GetColor3d("Black"))
        image_viewer.GetRenderWindow().SetSize(800, 800)
        image_viewer.GetRenderWindow().SetWindowName("ReadDICOMSeries")
        image_viewer.Render()
        qvtk.Start()


  




    def initUI(self):
        pass












if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
