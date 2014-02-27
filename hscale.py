##
# hscale.py
# Demo with an horizontal scale and an arrow which changes its
# length interactively according to the scale value
#

from tkinter import *

from infrastructure import DemoWindow,demo_path

class HorizontalScaleDemo(DemoWindow):

    def __init__(self):
        l = """An arrow and an horizontal scale are
        displayed below.  If you click or drag
        mouse button 1 in the scale, you can
        change the size of the arrow."""
        DemoWindow.__init__(self, l, demo_path('hscale.py'))

        self.frame = Frame(self,width=550,height=300)
        self.frame.pack(expand=Y,fill=BOTH)

        self.scale = Scale(self.frame, orient='horizontal',
                           length=300,
                           from_=0, to_=250, tickinterval=50,
                           command=self.scale_callback )
        self.scale.pack(side=TOP,expand=Y, fill=Y,
                        padx=30)
        self.canvas = Canvas( self.frame, height=150, width=320 )
        self.canvas.pack(side=LEFT,expand=Y, fill=BOTH )
        options={'fill':'cyan', 'outline':'darkblue' }
        self.arrow = self.canvas.create_polygon( *self.arrow_points(50) )
        self.canvas.itemconfigure( self.arrow, options )
        self.scale.set(50)


    def arrow_points ( self, l ):
        return ( 50, 75,
                 50, 125,
                 50+0.8*l, 125,
                 50+0.8*l, 140,
                 50+l, 100,
                 50+0.8*l, 60,
                 50+0.8*l, 75,
                 50, 75 )
                            
    def scale_callback(self, *others):
        v = self.scale.get()
        self.canvas.coords (self.arrow, *self.arrow_points(v) )


runDemo = HorizontalScaleDemo


## ----------------------------------------------------------------------------

if __name__ == '__main__' :
    demo = HorizontalScaleDemo()
    mainloop()






