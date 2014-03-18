# --- file : common.py
# This module contains commonly used classes
# 

from tkinter import *
from tkinter.ttk import *

class HScrollList(Frame):
    """This class combines a Listbox and a scroll list
    to obtain a verticlly scrollable list
    """
    def __init__(self,master):
        Frame.__init__(self,master)
        self.list = Listbox(self)
        self.list.pack(side=LEFT, expand=YES, fill=BOTH)
        self.scrollbar = Scrollbar(self,command=self.list.yview)
        self.list['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.pack(side=LEFT, fill=Y)
            
## ----------------------------------------------------------------------------
class TextTag:
    "A simple class to facilitate the creation of text tags."
    number=0
    def __init__(self, text_widget, **config ):
        self.id = TextTag.number
        TextTag.number = TextTag.number+1
        text_widget.tag_configure( self.id, config )

  
## ----------------------------------------------------------------------------
class DragCanvas ( Canvas ):
    """
    A canvas with default bindings which implements
    the dragging of selected canvas items.
    """
    COLOR_SELECTED='red'
    
    def __init__(self, master, **options):
        Canvas.__init__(self, master, options )

    def set_draggable(self, *items):
        for itm in items:
            self.addtag_withtag('draggable', itm)
            self.tag_bind('draggable', '<Any-Enter>', self.enter_callback )
            self.tag_bind('draggable', '<Any-Leave>', self.leave_callback )
            self.tag_bind('draggable', '<B1-Motion>', self.move_callback )


    #
    # - callbacks
    #
    def enter_callback(self, event):
        self.oldx, self.oldy = (self.canvasx(event.x),
                                self.canvasy(event.y) )
        
        self.oldcolor = self.itemcget('current', 'fill' )
        self.itemconfigure('current', fill=DragCanvas.COLOR_SELECTED )


    def leave_callback(self,event):
        self.itemconfigure('current', fill=self.oldcolor )


    def move_callback(self,event):

        x,y = ( self.canvasx(event.x),
                self.canvasy(event.y) )
        
        dx,dy = x - self.oldx, y-self.oldy
        
        self.move('current', dx, dy )
        self.oldx, self.oldy = x,y


