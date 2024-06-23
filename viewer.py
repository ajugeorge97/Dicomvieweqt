
from PySide6.QtWidgets import QWidget,QHBoxLayout
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionImage import vtkImageViewer2
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk_interaction import MyVtkInteractorStyleImage,StatusMessage

import vtkmodules.vtkRenderingContextOpenGL2
from vtkmodules.vtkRenderingCore import (
    vtkActor2D,
    vtkRenderWindowInteractor,
    vtkTextMapper,
    vtkTextProperty
    )



class Viewer(QWidget):
    def __init__(self) :
        super().__init__()
        self.reader=None
        self.testing=None

    def update_reader(self,folder):
        if not self.reader:
            self.reader = vtkDICOMImageReader()
        self.reader.SetDirectoryName(folder)
        self.reader.Update()
        



    def create_widgets(self,viewer):
        # self.reader = vtkDICOMImageReader()
        # self.testing="testing"
        # print(self.testing)
        # self.reader.SetDirectoryName(folder)
        # self.reader.Update()
        self.colors = vtkNamedColors()
        self.QHBoxLayout_viewer = QHBoxLayout()
        self.QHBoxLayout_viewer.setContentsMargins(0,0,0,0)

        self.qvtk=QVTKRenderWindowInteractor(viewer)
        self.QHBoxLayout_viewer.addWidget(self.qvtk)
        return self.QHBoxLayout_viewer




    def initUI(self):
        self.image_viewer = vtkImageViewer2()

        self.image_viewer.SetRenderWindow(self.qvtk.GetRenderWindow())
        self.image_viewer.SetInputConnection(self.reader.GetOutputPort())
        self.image_viewer.GetRenderer().ResetCamera()
        #self.image_viewer.SetSlice(0)
       
        my_interactor_style = MyVtkInteractorStyleImage()
    
        #Make imageviewer2 and sliceTextMapper visible to our interactorstyle
        #to enable slice status message updates when  scrolling through the slices.
        my_interactor_style.set_imageviewer(self.image_viewer)
        slice_text_prop = vtkTextProperty()
        slice_text_prop.SetFontFamilyToCourier()
        slice_text_prop.SetFontSize(20)
        slice_text_prop.SetVerticalJustificationToBottom()
        slice_text_prop.SetJustificationToLeft()
        # print(self.image_viewer.GetColorLevel())
        # Slice status message
        slice_text_mapper = vtkTextMapper()
        slice_text_mapper.SetTextProperty(slice_text_prop)

        slice_text_actor = vtkActor2D()
        slice_text_actor.SetMapper(slice_text_mapper)
        slice_text_actor.SetPosition(15,10)


        my_interactor_style.set_status_mapper(slice_text_mapper)

        #Make the interactor use our own interactorstyle
        #cause SetupInteractor() is defining it's own default interatorstyle
        #this must be called after SetupInteractor().
        #renderWindowInteractor.SetInteractorStyle(myInteractorStyle);
        self.image_viewer.SetupInteractor(self.qvtk)
        self.qvtk.SetInteractorStyle(my_interactor_style)
        self.qvtk.Render()

        #Add slice status message and usage hint message to the renderer.

        # Initialize rendering and interaction.
        self.image_viewer.GetRenderer().AddActor2D(slice_text_actor)

        self.image_viewer.Render()
        self.image_viewer.GetRenderer().ResetCamera()
        self.image_viewer.GetRenderer().SetBackground(self.colors.GetColor3d("Black"))
        self.image_viewer.GetRenderWindow().SetSize(800, 800)
        self.image_viewer.GetRenderWindow().SetWindowName("ReadDICOMSeries")
        self.image_viewer.Render()
        self.qvtk.Start()
     