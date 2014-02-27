
# -- canvas-plot.py
# A simple plot implemented using canvas
# Note that separate classes are used for the canvas and for its main
# window, so that thye canvas can also be embedded in the text demo
#

from tkinter import *
from infrastructure import DemoWindow

class CanvasPlot(Canvas):
    "A canvas implementing a simple plot"

    def __init__(self, master ):
        Canvas.__init__(self, master )
        self.configure({'width':450, 'height':300, 'cursor':'top_left_arrow'})

        self.title=self.create_text(225,20, text='A simple plot',
                                    font='helvetica 18', fill='brown' )
        
        # draw the x and y  axis
        self.line1=self.create_line(100, 250, 400, 250, width=2 )
        self.line2=self.create_line(100,250, 100, 50, width=2 )

        for i in range(1,11):
            x = 100+i*30
            self.create_line(x, 250, x, 245, width=2)
            self.create_text(x, 254, text=str(i*10), anchor='n',
                             font='helvetica 16' )
        
        for i in range(0,6):
            y = 250-i*40
            l = self.create_line(100, y, 105, y, width=2)
            t = self.create_text(96, y, text=str(i)+'.0', anchor='e',
                                 font='helvetica 16' )

            

        # draw the points
        points = [(12, 56), (20, 94), (33, 98), (32, 120),
                  (61, 180), (75, 160), (98, 223) ]
        
        self.items=[]
        for p0, p1 in points:
            x = 100 + 3*p0
            y = 250 - 4*p1/5

            itm = self.create_oval(x-6,y-6,x+6, y+6,
                                   width=1, outline='black',
                                   fill='SkyBlue2')
            self.addtag_withtag('points', itm )
            self.items.append(itm)

        
        # collectively bind the points, using the tag
        self.tag_bind('points', '<Any-Enter>', self.enter_callback )
        self.tag_bind('points', '<Any-Leave>', self.leave_callback )
        self.tag_bind('points', '<B1-Motion>', self.move_callback )

    #
    # callbacks
    #
    def enter_callback( self, event ):
        self.itemconfigure('current', fill='red' )
        self.oldx,self.oldy = self.canvasx(event.x), self.canvasy(event.y)

    def leave_callback( self, event ):
        self.itemconfigure('current', fill='SkyBlue2' )

    def move_callback( self, event ):
        x,y = self.canvasx(event.x), self.canvasy(event.y)
        self.move('current', x-self.oldx, y-self.oldy )
        self.oldx, self.oldy = x, y
        

    

class PlotDemoWindow(DemoWindow):

    def __init__(self ):
        l = """This window displays a canvas widget containing a
        simple 2-dimensional plot.  You can doctor the data by
        dragging any of the points with mouse button 1."""

        DemoWindow.__init__(self,l, 'canvasplot.py')

        self.canvas = CanvasPlot(self)
        self.canvas.pack(side=TOP)




runDemo = PlotDemoWindow

if __name__ == '__main__':
    demo = PlotDemoWindow()
    mainloop()


        
    
