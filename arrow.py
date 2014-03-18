##
# --- arrow-head.py
# A demo allowing to interactively observe the effects of
# any given arrow head shape definition.
# NOTE : contrary to the original tcl/tk demo, I don't re-draw
# everithing any time something is changed. Instead, I
# try to minimize changes, by reconfiguring affected
# canvas items.
# --

from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow
from common import DragCanvas

# some 'constants' [I know, ... ]


ARROW_X1 = 30
ARROW_Y = 120
ARROW_X2 = 320

SMALLTIPS = (4,5,4)

MAX_ARROW_WIDTH=200 
MAX_HEAD_HEIGHT=100 
MAX_HEAD_LENGTH=300

def scale_down (dim, scale):
    "Transform dimentions from 'magnified' to real"
    if type(dim) in ( tuple, list ):
        res=[]
        for x in dim:
            res.append(x/scale)
        return tuple(res)
    else:
        return dim//scale


class ArrowHeadCanvas( DragCanvas ):
    """A canvas to edit arrow heads.
    """
    def __init__(self, master, **options):
        DragCanvas.__init__(self, master)
        self.configure(options)

        # create thye separation line
        self.create_line( 350,0,350,350,width=2 )

        self.scale = 10 # magnify factor for big arrow
        # create the big arrow
        self.arrow_width=20
        self.arrow_shape = (80, 100, 30 )
        self.big_arrow = self.create_line(
            ARROW_X1, ARROW_Y, ARROW_X2, ARROW_Y,
            width=self.arrow_width,
            arrow='last',
            arrowshape = self.arrow_shape,
            fill = 'SkyBlue1' )

        # create the canvas items related to the arrow width
        self.width_arrow, self.width_box = None, None
        self.width_text, self.width_smalltext= None, None
        self.draw_arrow_width_controls()
        

        # create the canvas items related to the arrow head
        ( self.outline,
          self.height_arrow, self.minlen_arrow, self.maxlen_arrow,
          self.height_smalltext, self.minlen_smalltext,
          self.maxlen_smalltext,
          self.shape_box1, self.shape_box2,
          self.shape_text) = 10 * (None,)
        
        self.draw_arrow_head_controls()
        
        # bind the reshaping boxes to the proper callback
        self.set_draggable(self.gettags('reshape') )

        
        # create the little demo arrows at 'real dimensions'
        self.sample_arrows = None
        self.draw_sample_arrows()
        
        
        # create the labels showing current parameters



    def draw_sample_arrows(self):
        if not self.sample_arrows:
            self.sample_arrows = []
            for x1,y1,x2,y2 in ( (400, 30, 400, 80),
                       (375, 160, 425, 160),
                       (375,240,435,290) ):
                a = self.create_line (
                    x1,y1,x2,y2,
                    width=scale_down(self.arrow_width, self.scale ),
                    arrow='both',
                    arrowshape=scale_down(self.arrow_shape, self.scale) )
                self.sample_arrows.append(a)
        else:
            for a in self.sample_arrows :
                self.itemconfigure(
                    a,
                    width=scale_down(self.arrow_width, self.scale ),
                    arrowshape=scale_down(self.arrow_shape, self.scale) )
                                    
        

    def draw_arrow_head_controls(self):
        "Draws or re-draw the canavs items related to the arrow head"

        # create/update the two 'reshape box'
        x,y = ARROW_X2-self.arrow_shape[0], ARROW_Y
        if not self.shape_box1 :
            self.shape_box1 = self.create_rectangle(
                x-4,y-4,x+4,y+4, tags='reshape' )
        else:
            self.coords(self.shape_box1,
                        x-4,y-4,x+4,y+4 )

        x,y = (ARROW_X2-self.arrow_shape[1],
               ARROW_Y-self.arrow_width/2-self.arrow_shape[2] )
        if not self.shape_box2 :
            self.shape_box2 = self.create_rectangle(
                x-4,y-4,x+4,y+4, tags='reshape' )
        else:
            self.coords(self.shape_box2,
                        x-4,y-4,x+4,y+4 )


        # create the 'min head length' arrow and small text
        minlen = self.arrow_shape[0]
        w, h = self.arrow_width, self.arrow_shape[2]
        x1,y1,x2,y2 =  (ARROW_X2-minlen, ARROW_Y+w/2+h+30,
                        ARROW_X2, ARROW_Y+w/2+h+30 )
        
        if not self.minlen_arrow:
            self.minlen_arrow = self.create_line(
                x1,y1,x2,y2,
                arrow='both', arrowshape=SMALLTIPS )
        else:
            self.coords(self.minlen_arrow, x1,y1,x2,y2)


        x,y = ARROW_X2-minlen/2, ARROW_Y+w/2+h+40
        text=str(scale_down(minlen, self.scale)),
        if not self.minlen_smalltext:
            self.minlen_smalltext = self.create_text(
                x,y,
                text=text,
                anchor='c' )
        else:
            self.coords(self.minlen_smalltext,x,y)
            self.itemconfigure(self.minlen_smalltext, text=text )
            

        # create the 'max head length' arrow and small text
        maxlen = self.arrow_shape[1]
        w, h = self.arrow_width, self.arrow_shape[2]
        x1,y1,x2,y2 = (ARROW_X2-maxlen, ARROW_Y+w/2+h+50,
                       ARROW_X2, ARROW_Y+w/2+h+50 )
        if not self.maxlen_arrow:
            self.maxlen_arrow = self.create_line(
                x1,y1,x2,y2,
                arrow='both', arrowshape=SMALLTIPS )
        else:
            self.coords(self.maxlen_arrow, x1,y1,x2,y2)

        x,y = ARROW_X2-maxlen/2, ARROW_Y+w/2+h+60     
        text=str(scale_down(maxlen, self.scale))
        if not self.maxlen_smalltext:
            self.maxlen_smalltext = self.create_text(
                x,y, text=text, anchor='c' )
        else:
            self.coords(self.maxlen_smalltext,
                        x,y )
            self.itemconfigure(self.maxlen_smalltext,
                               text=text ) 
            
        # create the 'head height' arrow and small text
        height = self.arrow_shape[2]
        w = self.arrow_width
        x1,y1,x2,y2 = ARROW_X2+5, ARROW_Y-w/2, ARROW_X2+5, ARROW_Y-w/2-height,

        if not self.height_arrow :
            self.height_arrow = self.create_line(
                x1,y1,x2,y2,
                arrow='both', arrowshape=SMALLTIPS )
        else:
            self.coords(self.height_arrow, x1,y1,x2,y2)

        x,y = ARROW_X2+15, ARROW_Y-w/2-height/2
        text=str(scale_down(height, self.scale))       
        if not self.height_smalltext:
            self.height_smalltext = self.create_text(
                x,y, text=text,anchor='e' )
        else:
            self.coords(self.height_smalltext, x, y )
            self.itemconfigure(self.height_smalltext, text=text )


        # draw the arrow outilne
        coords = (
            ARROW_X2-self.arrow_shape[0],
            ARROW_Y,
            
            ARROW_X2-self.arrow_shape[1],
            ARROW_Y-self.arrow_width/2-self.arrow_shape[2],
            
            ARROW_X2, ARROW_Y,
            ARROW_X2-self.arrow_shape[1],
            
            ARROW_Y+self.arrow_width/2+self.arrow_shape[2],
            ARROW_X2-self.arrow_shape[0], ARROW_Y )
        
        options = {'width':2}
        
        if self.outline:
            self.coords( self.outline, coords )
        else:
            self.outline = self.create_line(*coords, **options) 


        # create/update the label showing the head parameters
        font = '-*-Helvetica-Medium-R-Normal--*-140-*-*-*-*-*-*'
        shape = scale_down(self.arrow_shape, self.scale )
        
        if not self.shape_text:
            self.create_text( 30, 330, text='arrowshape = ',
                                 font=font, anchor='w' )
            self.shape_text=self.create_text( 150, 330,
                                          text = str(shape),
                                          font=font, anchor='w' )
        else:
            self.itemconfigure(self.shape_text, text=str(shape) )


            
    def draw_arrow_width_controls(self):

        w = self.arrow_width

        # create/update the 'arrow width box'
        x,y = ARROW_X1, ARROW_Y-w/2
        if not self.width_box:
            self.width_box = self.create_rectangle(
                x-4,y-4,x+4,y+4, tags='reshape' )
        else:
            self.coords(self.width_box, x-4,y-4,x+4,y+4)
        

        # create/update the width arrow
        coords = (ARROW_X1-5, ARROW_Y-w/2, ARROW_X1-5, ARROW_Y+w/2)
    
        if  not self.width_arrow:
            options = {'arrow':'both', 'arrowshape':SMALLTIPS}
           
            self.width_arrow = self.create_line (*(coords, options))
                                    
        else:
            self.coords(self.width_arrow, coords )


        # create/update the width small text
        coords = (ARROW_X1-10, ARROW_Y)
        options = {'text':str(scale_down(self.arrow_width, self.scale)),
                   'anchor':'e' }
        
        if not self.width_smalltext:
            self.width_smalltext = self.create_text (*coords, **options )
        else:
            self.itemconfigure(self.width_smalltext,
                               options )


        # create/update the label showing the width
        w = scale_down(self.arrow_width, self.scale )
        
        if not self.width_text :
            font = '-*-Helvetica-Medium-R-Normal--*-140-*-*-*-*-*-*'
            self.create_text( 30, 310, text='width = ',
                                 font=font, anchor='w' )
            self.width_text=self.create_text( 150, 310,
                                          text = str(w),
                                          font=font, anchor='w' )
        else:
            self.itemconfigure(self.width_text, text=str(w) )

        

    def move_callback(self,event):
        """Re-implementation of the parent callback.
        It is called when one of the 'reshaping boxes' is dragged
        """
        x,y = self.canvasx(event.x), self.canvasy(event.y)
        dx, dy = x-self.oldx, y-self.oldy

        current, = self.find_withtag('current')

        if current == self.width_box : # user is changing arrow width

            dx = 0 # movement allowed only on y axis
            
            # round dy to a multiple of the scale
            dy = int (dy / self.scale )*self.scale

            # check width limits
            if( self.arrow_width - dy < 0 ):
                dy = self.arrow_width
            if ( self.arrow_width - dy > MAX_ARROW_WIDTH ):
                dy = self.arrow_width-MAX_ARROW_WIDTH

            # apply the new width
            self.change_arrow_width( self.arrow_width-dy )

        elif current == self.shape_box1 : # user is changing head length1

            dy = 0 # only horizontal movements allowed
            dx = int(dx/self.scale)*self.scale # rounded

            #check boundaries
            if self.arrow_shape[0] - dx < 0 :
                dx = self.arrow_shape[0]                                      
            if self.arrow_shape[0] - dx > MAX_HEAD_LENGTH:
                dx = MAX_HEAD_LENGTH - self.arrow_shape[0]

            # apply changes
            self.change_head_shape( self.arrow_shape[0] - dx,
                                    self.arrow_shape[1],
                                    self.arrow_shape[2]  )

        elif current == self.shape_box2 : # user is changing length2 and height
            
            # round dx and dy
            dx = int(dx/self.scale)*self.scale
            dy = int(dy/self.scale)*self.scale

            #check boundaries
            if self.arrow_shape[1] - dx < 0 :
                dx = self.arrow_shape[1]                                      
            if self.arrow_shape[1] - dx > MAX_HEAD_LENGTH:
                dx = MAX_HEAD_LENGTH - self.arrow_shape[1]
        
            if self.arrow_shape[2] - dy < 0 :
                dy = self.arrow_shape[2]                                      
            if self.arrow_shape[2] - dy > MAX_HEAD_HEIGHT:
                dy = MAX_HEAD_HEIGHT - self.arrow_shape[Y]

            # apply changes
            self.change_head_shape( self.arrow_shape[0],
                                    self.arrow_shape[1] - dx,
                                    self.arrow_shape[2] - dy )

        # move the box 
        self.move( 'current', dx, dy )
        self.oldx = self.oldx + dx
        self.oldy = self.oldy + dy
        



    def change_arrow_width( self, width ):
        self.arrow_width=width
        self.itemconfigure(self.big_arrow, width=width )

        # redraw sample arrows
        self.draw_sample_arrows()

        # redrow width controls
        self.draw_arrow_width_controls()
                    
        # re-draw other elements affected by width change
        self.draw_arrow_head_controls()



    def change_head_shape( self, len1, len2, height ):
        self.arrow_shape = (len1, len2, height)
        
        self.itemconfigure(self.big_arrow, arrowshape=self.arrow_shape )

        # redraw sample arrows
        self.draw_sample_arrows()
                    
        # re-draw other elements affected by width change
        self.draw_arrow_head_controls()



class ArrowHeadDemo (DemoWindow):

    def __init__(self):
        l = """This widget allows you to experiment with different
        widths and arrowhead shapes for lines in canvases.
        To change the line width or the shape of the arrowhead,
        drag any of the three boxes attached to the oversized arrow.
        The arrows on the right give examples at normal scale.
        The text at the bottom shows the configuration options as
        you'd enter them for a canvas line item
        """

        DemoWindow.__init__(self,l,'arrow.py' )
        
        self.canvas = ArrowHeadCanvas(self, relief=SUNKEN, border=2,
                             height=350, width=450)
        self.canvas.pack(side=TOP, expand=YES, fill=BOTH )


#entry point for widget main module        
runDemo = ArrowHeadDemo
    
## ====================================================================
if __name__ == '__main__':
    demo = ArrowHeadDemo()
    mainloop()

