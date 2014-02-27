from tkinter import *

from infrastructure import DemoWindow, demo_path
import tkinter.messagebox as messagebox

SCROLLAREA_HEIGHT=1024
SCROLLAREA_WIDTH=1280

ROW_NUM=10
COLUMN_NUM=16

ROW_PAD=30
COLUMN_PAD=30

BOX_HEIGHT=(SCROLLAREA_HEIGHT/COLUMN_NUM) - COLUMN_PAD
BOX_WIDTH =(SCROLLAREA_WIDTH/ROW_NUM) - ROW_PAD

CURRENTBOX_COLOR = 'cyan'
BOX_COLOR = 'lightgray'


class ScrollableCanvas( Frame ):
    """A canvas with scroll bars. A number of
    box is drawn inside the canvas to fill it.
    """

    def __init__(self, master):
        Frame.__init__(self,master)

        # create and pack the canvas and the two scrollbars
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        self.canvas = Canvas(self, relief=SUNKEN, border=2,
                             scrollregion=(0,0,1280,1024) )
        self.vbar=Scrollbar(self, command=self.canvas.yview)
        self.hbar=Scrollbar(self, orient='horizontal',
                            command=self.canvas.xview )
        self.canvas.configure({'xscrollcommand':self.hbar.set,
                               'yscrollcommand':self.vbar.set} )
        self.canvas.grid(row=0,column=0, sticky='nsew' )
        self.vbar.grid(row=0,column=1,sticky='ns' )
        self.hbar.grid(row=1,column=0,sticky='ew' )

        self.fill_canvas()


    def fill_canvas(self):
        for r in range(0,ROW_NUM):
            x = ROW_PAD+(r*(BOX_WIDTH+ROW_PAD))
            for c in range(0,COLUMN_NUM):
                y = COLUMN_PAD+c*(BOX_HEIGHT+COLUMN_PAD)
                name = '%d,%d'% (c,r)

                # Note : if fill option was omitted, the rectangle
                # would have created empty. This means tha only the
                # outline would have generated events
                id = self.canvas.create_rectangle(x, y,
                                      x+BOX_WIDTH, y+BOX_HEIGHT,
                                      fill=BOX_COLOR, tags=('box', name ) )
                self.canvas.create_text(x+BOX_WIDTH/2,y+BOX_HEIGHT/2,
                                        anchor='c', text=name,
                                        tags='text' )

                
        self.canvas.tag_bind('all', '<Any-Enter>', self.enter_callback )
        self.canvas.tag_bind('all', '<Any-Leave>', self.leave_callback )
        self.canvas.tag_bind('all', '<1>', self.select_callback )
        self.canvas.tag_bind('all', '<3>', self.scanmark_callback )
        self.canvas.tag_bind('all', '<B3-Motion>', self.scandragto_callback )

    def get_current_box(self):
        id, = self.canvas.find_withtag('current')
        tags = self.canvas.gettags('current')
##        print 'tags of selected ='+`tags`
        if 'text' in tags: # the current item is the text in the box
            id = self.canvas.find_withtag(self.canvas.itemcget(id,'text'))

        return id



    def enter_callback(self, event):
        id = self.get_current_box()
        self.canvas.itemconfigure(id, fill=CURRENTBOX_COLOR)


    def leave_callback(self,event):
        id = self.get_current_box()
        self.canvas.itemconfigure(id, fill=BOX_COLOR)


    def scanmark_callback( self,event ):
        self.canvas.scan_mark(event.x, event.y)

    def scandragto_callback(self,event):
        self.canvas.scan_dragto(event.x, event.y)

                 
    def select_callback( self,event):
        id = self.get_current_box()
        tags=self.canvas.gettags('current')
        for t in tags:
            if t not in ('current','box'):
                box_name=t
                    
        messagebox.showinfo(
            title='Box clicked',
            message='You have clicked on box:'+box_name)
                              
                              

class ScrollCanvasDemo ( DemoWindow ):

    def __init__(self):
        l = """This window displays a canvas widget that can be
        scrolled either using the scrollbars or by dragging with
        button 2 in the canvas.  If you click button 1 on one of
        the rectangles, its indices will displayed.
        You can also drag with button 3 to scroll the canvas.
        """
        DemoWindow.__init__(self,l,demo_path('canvasscroll.py') )

        self.canvas = ScrollableCanvas(self)
        self.canvas.pack(expand='Y', fill='both' )


runDemo =  ScrollCanvasDemo


## ----------------------------------------------------------------------------

if __name__ == '__main__':
    demo = ScrollCanvasDemo()
    mainloop()
