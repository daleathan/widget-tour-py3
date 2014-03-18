
from tkinter import *

from infrastructure import DemoWindow
from common import DragCanvas


class CanvasItemDemo(DemoWindow):
    """A canvas with lots of items of any type which
    can be dragged around"""

    def __init__(self):
        l = """This window contains a canvas widget with examples of the
        various kinds of items supported by canvases.  The following
        operations are supported:
             Button-1 drag: moves item under pointer.
             Button-2 drag: repositions view.       
             Button-3 drag: strokes out area.       
             Ctrl+f:        prints items under area. 
        """
        DemoWindow.__init__(self,l, 'items.py' )

        #create the canvas and the scroll bars
        frame = Frame(self); frame.pack(expand=YES, fill=BOTH )
        self.canvas=DragCanvas(frame, scrollregion=(0,0,'30c','24c'),
                           relief=SUNKEN, border=2,width='15c',height='10c' )
        hbar = Scrollbar(frame, orient='horiz', command=self.canvas.xview)
        vbar=Scrollbar(frame, command=self.canvas.yview)
        self.canvas.configure({'xscrollcommand':hbar.set,
                               'yscrollcommand':vbar.set} )
        frame.rowconfigure(0, weight=1 )
        frame.columnconfigure(0, weight=1 )
        self.canvas.grid(row=0,column=0, sticky='nsew')
        hbar.grid(row=1,column=0, sticky='ew')
        vbar.grid(row=0,column=1, sticky='ns' )

        # create grid lines
        width, height = 30,24; unit='c'
        nrow, ncol = 3,2
        dx, dy = width/ncol, height/nrow
        self.canvas.create_rectangle( 0, 0, `width`+unit, `height`+unit,
                                      width=2 )
        for i in range(1,nrow):
            x1,y1,x2,y2 = 0,dy*i,width, dy*i
            self.canvas.create_line( `x1`+unit, `y1`+unit,
                                     `x2`+unit, `y2`+unit,
                                     width=2 )
        for i in range(1,ncol):
            x1,y1,x2,y2 = dx*i,0,dx*i,height
            self.canvas.create_line( `x1`+unit, `y1`+unit,
                                     `x2`+unit, `y2`+unit,
                                     width=2 )

        # this procedure is getting quite lengthy
        # better define sub-procedure to create the various items
        # the arguments define the canvas sub-area to use
        self.create_lines( 0, 0, dx, dy, unit )

        self.canvas.set_draggable(self.canvas.gettags('item'))
        # bind collectively all items tagged with 'item'
#        self.canvas.tag_bind('item','<Any-Enter>', self.enter_callback )
#        self.canvas.tag_bind('item', '<Any-Leave>', self.leave_callback )
#        self.canvas.tag_bind('item', '<B1-Motion>', self.move_callback )


    # A little funct to apply the unit at a list of
    # numbers, i.e converting (8,24) in ('8c', '24c')
    # So that I can keep coordinates as numbers 
    def apply_unit(self, list, unit ):
        global u
        u=unit
        return map( lambda x: `x`+u,
                    list )

    #
    # -- sub-procedures creating the canvas items
    #
    
    def create_lines(self, x1, y1, dx, dy, unit):
        tx, ty = x1+dx/2, y1+0.1
        self.canvas.create_text(`tx`+unit,`ty`+unit,
                                text='Lines', anchor='n' )

        # draw the z-shaped spline
        z_width, z_height = dx/4, dy/3
        z_x, z_y = x1+dx/10, y1+dy/10

        # a rather indirect call of self.canvas.create_line
        # which allows me to avoid appending the unit to each
        # number (I'll use later, too )
        points = self.apply_unit(
            (z_x, z_y, z_x+z_width, z_y,
             z_x, z_y+z_height, z_x+z_width, z_y+z_height ),
            unit )
        options = {'width':4, 'fill':'blue', 'tags':'item' }
        apply( self.canvas.create_line, (points, options) )

        # draw the two arrow-head lines
        points= self.apply_unit(
            (x1+dx/1.8, y1+dy/0.2, x1+dx/1.8, y1+dy/2.2 ),
            unit )
        options = { 'width':1, 'arrow':'last', 'tags':'item' }
        apply(self.canvas.create_line, (points, options) )
        
    #
    # -- callbacks
    #





runDemo = CanvasItemDemo


## ------------------------------------------------------------------------

if __name__ == '__main__':
    demo = CanvasItemDemo()
    mainloop()

