#!/usr/bin/env python3

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

#Helper class to format slice status message
class StatusMessage:
    @staticmethod
    def format(slice:int,max_slice:int):
        return f"Slice Number {slice+1}/{max_slice+1}"
    
#Define own interaction style
class MyVtkInteractorStyleImage(vtkInteractorStyleImage):
    def __init__(self,parent=None):
        super().__init__()
        self.AddObserver("KeyPressEvent", self.keyPressEvent)
        self.AddObserver("MouseWheelForwardEvent", self.mouseWheelForwardEvent)
        self.AddObserver("MouseWheelBackwardEvent", self.mouseWheelBackwardEvent)
        self.imageviewer=None
        self.status_mapper=None
        self.slice=0
        self.min_slice=0
        self.max_slice=0
    
    def set_imageviewer(self, image_viewer):
        self.imageviewer=image_viewer
        self.min_slice=image_viewer.GetSliceMin()
        self.max_slice=image_viewer.GetSliceMax()
        self.slice=self.min_slice
        print(f"Slicer: Min = {self.min_slice}, Max= {self.max_slice}")

    def set_status_mapper(self, status_mapper):
        self.status_mapper=status_mapper

    def move_slice_forward(self): 
        if self.slice<self.max_slice:
            self.slice+=1
            print(f"MoveSliceForward :: Slice = {self.slice}")
            self.imageviewer.SetSlice(self.slice)
            msg=StatusMessage.format(self.slice,self.max_slice)
            self.status_mapper.SetInput(msg)
            self.imageviewer.Render()

    def move_slice_backward(self):
        if self.slice>self.min_slice:
            self.slice-=1
            print(f"MoveSliceBackrward :: Slice = {self.slice}")
            self.imageviewer.SetSlice(self.slice)
            msg=StatusMessage.format(self.slice,self.max_slice)
            self.status_mapper.SetInput(msg)
            self.imageviewer.Render()

    def keyPressEvent(self,obj,event):
        key=self.GetInteractor().GetKeySym()
        if key=="Up":
            self.move_slice_forward() 
        elif key=="Down":
            self.move_slice_backward()

    def mouseWheelForwardEvent(self,obj,event):
        self.move_slice_forward()

    def mouseWheelBackwardEvent(self,obj,event) :
        self.move_slice_backward()