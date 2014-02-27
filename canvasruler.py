##
# -- canvas-rulr.py
# A canvas with a ruler drawn in it.
# You can add and delete tabs, via drag&drop
#

from tkinter import *

from infrastructure import DemoWindow, demo_path


RULER_UNITS = 10
RULER_TICKS = 4*RULER_UNITS

RULER_LENGTH=400
TICK_LENGTH = RULER_LENGTH//RULER_TICKS
RULER_START=30
RULER_END=RULER_START+RULER_LENGTH

TAB_Y = 60


STIPPLE_BITMAP_FILE=demo_path('images/gray25.bmp')

#
# Note : for some reason, this generates TclError 'bitmap XXXX not defined'
# when used either direcly or via 'name' attribute, so I used raw tk commands
# instead
#
# STIPPLE_BITMAP = BitmapImage(master=Tk(),file=STIPPLE_BITMAP_FILE)
#


#
# Note : to execute the Tk command, I need to create a Toplevel window
# I guess I could use the toplevel create in widget.py, buth then this
# module would not run stand-alone
#
temp = Tk()
STIPPLE_BITMAP = temp.tk.eval(
            'image create bitmap @%s' % STIPPLE_BITMAP_FILE )
## Now I can delete the spurious window
temp.destroy()


TAB_NORMAL_STYLE = {'fill':'black', 'stipple':''}
TAB_INRANGE_STYLE = {'fill':'green', 'stipple':''}
TAB_OUTOFRANGE_STYLE = {'fill':'red', 'stipple':STIPPLE_BITMAP}


class RulerCanvas (Canvas):

    def __init__(self, master ):
        Canvas.__init__(self, master, width=200+RULER_LENGTH, height=100 )
        self.draw_ruler()
        self.draw_well()


    def draw_ruler(self):

        # draw the line
        self.create_line( RULER_START, 50, RULER_END, 50 )
        text=''
        for tick in range(0,RULER_TICKS+1):
            if tick % 4 == 0 : # unit thick
                h = 20
                text=str(tick//4)
                
            elif tick % 2 == 0 : # half unit tick
                h = 10                
            else:
                h = 5
                
            x = RULER_START + tick * TICK_LENGTH
            self.create_line( x, 50, x, 50-h )
            if text:
                self.create_text(x, 20, text=text )
                text=''


    def draw_tab(self, x, y ):
        id = self.create_polygon( x-8,y,x,y-8, x+8,y, tags='tab' )
        self.tag_bind(id, '<Any-Enter>', self.enter_callback )
        self.tag_bind(id, '<B1-ButtonRelease>', self.release_callback )
        self.tag_bind(id, '<B1-Motion>', self.move_callback )        
        return id

    def draw_well_tab( self ):
        self.well_tab = self.draw_tab( RULER_END+50, TAB_Y )
        
    def draw_well (self):
        x, y = RULER_END+40, TAB_Y
        self.well_box = self.create_rectangle( x,y+5,x+20,y-15 )
        self.well_x, self.well_y = x+10,y 
        self.draw_well_tab()



    def check_tab_coords(self, id ):
        x1,y1,x2,y2,x3,y3 = self.coords(id)
        return ( ( x2 >= RULER_START ) and
                 ( x2 <= RULER_END ) and
                 ( y1 >= TAB_Y-5 ) and
                 ( y1 <= TAB_Y+5 ) )

    def adjust_tab_coords( self, id ):
        x1,y1,x2,y2,x3,y3 = self.coords(id)
        dy = TAB_Y - y1
        round_x = int (x2 // TICK_LENGTH )*TICK_LENGTH
        if (x2-round_x) > TICK_LENGTH//2:
            round_x = round_x + TICK_LENGTH
        dx = round_x-x2

        return dx,dy
    


    def check_tab_position(self, id):
        if not self.check_tab_coords(id ):
            self.itemconfigure(id, TAB_OUTOFRANGE_STYLE )
        else:
            self.itemconfigure(id, TAB_INRANGE_STYLE )
            dx, dy = self.adjust_tab_coords(id)
            self.move(id, dx,dy )
            self.oldx, self.oldy = self.oldx+dx, self.oldy+dy



    def enter_callback(self, event):
        id, = self.find_withtag('current')
        self.oldx, self.oldy = self.canvasx(event.x),self.canvasy(event.y)
        self.itemconfigure('current', TAB_NORMAL_STYLE )
        self.check_tab_position(id)


    def move_callback(self,event):
        id, = self.find_withtag('current')
        x,y = self.canvasx(event.x), self.canvasy(event.y)
        dx,dy = x - self.oldx, y - self.oldy
        
        self.move(id, dx,dy )
        self.oldx, self.oldy = self.oldx+dx, self.oldy+dy
        self.check_tab_position(id)


    def release_callback(self, event):
        id, = self.find_withtag('current')
        if self.check_tab_coords(id) :
            self.itemconfigure('current', TAB_NORMAL_STYLE )
        else:
            self.delete(id)
            
        if id == self.well_tab :
            self.draw_well_tab()
        
            
    

class RulerDemo(DemoWindow):

    def __init__(self):
        l = """This canvas widget shows a mock-up of a ruler.
        You can create tab stops by dragging them out of the
        well to the right of the ruler.  You can also drag
        existing tab stops.  If you drag a tab stop far enough
        up or down so that it turns dim, it will be deleted when
        you release the mouse button."""
        DemoWindow.__init__(self, l, demo_path('canvasruler.py'))

        self.canvas = RulerCanvas(self)
        self.canvas.pack(expand=YES, fill=BOTH )


def runDemo():
    RulerDemo()


# ----------------------------------------------------------------------------

if __name__ == '__main__':
    demo = RulerDemo()
    mainloop()



