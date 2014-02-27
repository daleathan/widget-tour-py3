##
# v-scale.py
# Demo with a vertical scale and an arrow which changes its
# length interactively according to the scale value
#

from tkinter import *

from infrastructure import DemoWindow, demo_path

class VerticalScaleDemo(DemoWindow):

    def __init__(self):
        l = """An arrow and a vertical scale are
        displayed below.  If you click or drag
        mouse button 1 in the scale, you can
        change the size of the arrow."""
        DemoWindow.__init__(self, l, demo_path('vscale.py'))

        self.frame = Frame(self,width=300,height=500)
        self.frame.pack(expand=Y,fill=BOTH)

        self.scale = Scale(self.frame,
                           orient='vertical', length=300,
                           from_=0, to_=250, tickinterval=50,
                           command=self.scale_callback )
        
        self.scale.pack(side=LEFT,expand=Y, fill=Y,
                        padx=30, pady=30)
        self.canvas = Canvas( self.frame, height=300, width=200 )
        self.canvas.pack(side=LEFT,expand=Y, fill=BOTH )
        options={'fill':'cyan', 'outline':'darkblue' }
        self.arrow = self.canvas.create_polygon ( *self.arrow_points(50) )
        self.canvas.itemconfigure( self.arrow, options )
        self.scale.set(50)


    def arrow_points ( self, l ):
        return ( 75, 50,
                 125,50,
                 125, 50+0.8*l,
                 140, 50+0.8*l,
                 100, 50+l,
                 60, 50+0.8*l,
                 75, 50+0.8*l,
                 75, 50 )
                            
    def scale_callback(self, *others):
        v = self.scale.get()
        self.canvas.coords ( self.arrow, *self.arrow_points(v) )



runDemo = VerticalScaleDemo()

## ----------------------------------------------------------------------------

if __name__ == '__main__' :
    demo = VerticalScaleDemo()
    mainloop()


