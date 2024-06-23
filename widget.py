# This Python file uses the following encoding: utf-8
import sys
import sys
from PySide6.QtCore import Qt,QCoreApplication
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout,QSizePolicy,QMainWindow,QFileDialog
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
import vtkmodules.vtkRenderingContextOpenGL2
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
    vtkTextMapper,
    vtkTextProperty
    )

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from viewer import Viewer


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        
        self.ui.setupUi(self)
        self.showMaximized()

        self.load_dicom_series(self.ui.browse_button)

        self.reader = None
        self.image_viewer = None
        self.qvtk=None
        self.viewer_widget = None
    
    def onclick(self):
        #folder=r"Sampledata/digest_article"
        folder= QFileDialog.getExistingDirectory(None, "Open Folder", "./Sampledata")
        self.handle_image_viewer(self.ui.viewer, folder)

    def load_dicom_series(self,browse_button):
        browse_button.clicked.connect(self.onclick)



    def handle_image_viewer(self,viewer,folder):

        if self.viewer_widget is None:
            self.viewer_widget = Viewer()
    
        self.viewer_widget.update_reader(folder)

        viewer_layout= self.viewer_widget.create_widgets(viewer)
        viewer.setLayout(viewer_layout)
        self.viewer_widget.initUI()





        # if self.reader:
        #     self.reader=None
        # self.reader = vtkDICOMImageReader()
        # self.reader.SetDirectoryName(folder)
        # self.reader.Update()
        # colors=vtkNamedColors()
        # self.QHBoxLayout_viewer=QHBoxLayout()
        # self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)

        # self.qvtk=QVTKRenderWindowInteractor(viewer)
        # self.QHBoxLayout_viewer.addWidget(self.qvtk)
        # viewer.setLayout(self.QHBoxLayout_viewer)

        # #Visualilze
        # if self.image_viewer:
        #     self.image_viewer=None
        # self.image_viewer = vtkImageViewer2()

        # self.image_viewer.SetRenderWindow(self.qvtk.GetRenderWindow())
        # self.image_viewer.SetInputConnection(self.reader.GetOutputPort())
        # self.image_viewer.GetRenderer().ResetCamera()
        # #self.image_viewer.SetSlice(0)
        # #Slice status message 
        # slice_text_prop = vtkTextProperty()
        # slice_text_prop.SetFontFamilyToCourier()
        # slice_text_prop.SetFontSize(20)
        # slice_text_prop.SetVerticalJustificationToBottom()
        # slice_text_prop.SetJustificationToLeft()
        # print(self.image_viewer.GetColorLevel())
        # #Slice status message
        # slice_text_mapper = vtkTextMapper()
        # msg=StatusMessage.format(self.image_viewer.GetSliceMin(),self.image_viewer.GetSliceMax())
        # slice_text_mapper.SetInput(msg)
        # slice_text_mapper.SetTextProperty(slice_text_prop)  

        # slice_text_actor = vtkActor2D()
        # slice_text_actor.SetMapper(slice_text_mapper)
        # slice_text_actor.SetPosition(15,10)

        # #usage hint message 
        # usage_text_prop = vtkTextProperty()
        # usage_text_prop.SetFontFamilyToCourier()
        # usage_text_prop.SetFontSize(14)
        # usage_text_prop.SetVerticalJustificationToTop()
        # usage_text_prop.SetJustificationToLeft()
        # usage_text_mapper = vtkTextMapper()
        # usage_text_mapper.SetInput(
        #     "Slice with mouse wheel\n  or Up/Down-Key\n- Zoom with pressed right\n "
        #     " mouse button while dragging"
        # )
        # usage_text_mapper.SetTextProperty(usage_text_prop)

        # usage_text_actor = vtkActor2D ()
        # usage_text_actor.SetMapper(usage_text_mapper)
        # usage_text_actor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
        # usage_text_actor.GetPositionCoordinate().SetValue(0.05, 0.95)

        # #Create an interactor with our own style (inherit from
        # #vtkInteractorStyleImage in order to catch mousewheel and key events.
        # #render_window_interactor= vtkRenderWindowInteractor()

        # my_interactor_style = MyVtkInteractorStyleImage()
    
        # #Make imageviewer2 and sliceTextMapper visible to our interactorstyle
        # #to enable slice status message updates when  scrolling through the slices.
        # my_interactor_style.set_imageviewer(self.image_viewer)
        # my_interactor_style.set_status_mapper(slice_text_mapper)

        # #Make the interactor use our own interactorstyle
        # #cause SetupInteractor() is defining it's own default interatorstyle
        # #this must be called after SetupInteractor().
        # #renderWindowInteractor.SetInteractorStyle(myInteractorStyle);
        # self.image_viewer.SetupInteractor(self.qvtk)
        # self.qvtk.SetInteractorStyle(my_interactor_style)
        # self.qvtk.Render()

        # #Add slice status message and usage hint message to the renderer.
        # self.image_viewer.GetRenderer().AddActor2D(slice_text_actor)
        # self.image_viewer.GetRenderer().AddActor2D(usage_text_actor)

        # # Initialize rendering and interaction.
        # self.image_viewer.Render()
        # self.image_viewer.GetRenderer().ResetCamera()
        # self.image_viewer.GetRenderer().SetBackground(colors.GetColor3d("Black"))
        # self.image_viewer.GetRenderWindow().SetSize(800, 800)
        # self.image_viewer.GetRenderWindow().SetWindowName("ReadDICOMSeries")
        # self.image_viewer.Render()
        # self.qvtk.Start()

    def initUI(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.setWindowTitle("Dicom Viewer")
    sys.exit(app.exec())
