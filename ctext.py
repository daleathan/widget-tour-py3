##
# --- canvas-text.py
# A demo of text item capabilities in canvases
#

from tkinter import *

from infrastructure import DemoWindow, demo_path

CANVAS_HEIGHT=350
CANVAS_WIDTH=500

BOX_COLOR='lightblue'
BOX_SELECTED_COLOR='green'
BOX_LENGTH = 30

POSCTL_X = 100
POSCTL_Y = 100
POSCTL_TEXT_X = POSCTL_X
POSCTL_TEXT_Y = POSCTL_Y - 70

POSJ_X = 350
POSJ_Y = POSCTL_Y - BOX_LENGTH
POSJ_TEXT_X = POSJ_X
POSJ_TEXT_Y = POSCTL_TEXT_Y



TEXT_X = CANVAS_WIDTH/2
TEXT_Y = CANVAS_HEIGHT*2/3

# Text selection operations on canvas text requires strings of form @x,y which
# translates as 'the character which covers position x,y'
# In Tkinter there is a function At which does something like this
# However, some comments in the file makes me think that it will be
# obsoleted, so better don't use it
def at_string( x,y ):
    return '@%f,%f'% (x, y)


class EditableTextItem:
    def __init__(self, canvas, x, y, **options):
        self.canvas = canvas
        self.id = canvas.create_text( x, y, options ) 

        # this bunch of bindings is to make the text editable
        # The tcl code is more synthetic here, because it can
        # specify tcl callback code directly in the bind statement
        canvas.tag_bind( self.id, '<1>', self.b1press_callback )
        canvas.tag_bind( self.id, '<B1-Motion>', self.b1move_callback )
        canvas.tag_bind( self.id, '<Shift-1>', self.shiftb1_callback )
        canvas.tag_bind(self.id,'<Shift-B1-Motion>',self.shiftb1move_callback)
        canvas.tag_bind( self.id, '<KeyPress>', self.keypress_callback )
        canvas.tag_bind( self.id, '<Return>', self.return_callback )
        canvas.tag_bind( self.id, '<Control-h>', self.backspace_callback )
        canvas.tag_bind( self.id, '<BackSpace>', self.backspace_callback )
        canvas.tag_bind( self.id, '<Delete>', self.delchar_callback )
        canvas.tag_bind( self.id, '<2>', self.paste_callback )

    def delete_selection(self):
        try:
            self.canvas.dchars(self.id, 'sel.first', 'sel.last' )
            return 1
        except TclError: # no selection ro be deleted
            return 0
    

    def b1press_callback( self, event ):
        self.canvas.icursor('current', at_string(event.x, event.y) )
        self.canvas.focus('current')
        self.canvas.focus_set()
        self.canvas.select_from('current', at_string(event.x, event.y) )

    def b1move_callback(self, event):
        self.canvas.select_to('current', at_string(event.x, event.y) )
        
    def shiftb1_callback(self,event):
        self.canvas.select_adjust('current', at_string(event.x, event.y) )

    def shiftb1move_callback(self,event):
        self.canvas.select_to('current', at_string(event.x, event.y))

    def keypress_callback(self,event):
        self.canvas.insert(self.id, 'insert', event.char )

    def return_callback(self,event):
        self.canvas.insert(self.id, 'insert', '\n' )

    def backspace_callback(self,event):
        if not self.delete_selection():
            self.canvas.dchars( self.id,
                                self.canvas.index(self.id, 'insert' )-1 )

    def delchar_callback(self,event):
        if not self.delete_selection():
            self.canvas.dchars(self.id, 'insert')

    def paste_callback(self, event):
        self.canvas.insert(self.id,
                           at_string(event.x, event.y),
                           self.canvas.selection_get() )
        


class TextDemoCanvas( Canvas ):

    def __init__(self, master):
        Canvas.__init__(self, master,
                        height=CANVAS_HEIGHT, width=CANVAS_WIDTH,
                        relief=SUNKEN, border=2)

        self.create_text_controls()

        self.create_position_controls()

        self.create_justification_controls()
        
    def create_text_controls(self):
        txt = """
This is just a string of text to demonstrate the
text facilities of canvas widgets.
Bindings have been defined to support
editing (see above)."""

        self.create_rectangle( TEXT_X-3, TEXT_Y-3,
                               TEXT_X+3, TEXT_Y+3,
                               fill='red', outline='black' )
        self.text = EditableTextItem(self,
                                     TEXT_X, TEXT_Y,
                                     text=txt,
                                     anchor='c', justify='left',
                                     font='Times 24')


    def create_justification_controls(self):

        self.create_text(POSJ_TEXT_X, POSJ_TEXT_Y,
                         anchor='c', justify='center',
                         text='Justification',
                         font = 'Times 18' )

        j_tags = ('left','center','right' )

        for r in range(0,3):
            x = POSJ_X + (r-1)*BOX_LENGTH            
            y = POSJ_Y
            self.create_rectangle(
                x-0.5*BOX_LENGTH, y-0.5*BOX_LENGTH,
                x+0.5*BOX_LENGTH, y+0.5*BOX_LENGTH,
                fill=BOX_COLOR, outline='black',
                tag = ('jbox',j_tags[r]) )

        self.tag_bind('jbox', '<Any-Enter>', self.enter_callback )
        self.tag_bind('jbox', '<Any-Leave>', self.leave_callback )
        self.tag_bind('jbox', '<1>',self.setjustify_callback)            


    def create_position_controls(self):

        # strange but true : the 'ancor directions' are
        # exactly the contrary of usual 'map' direction:
        # north is down, and west is on the right (??)
        # Solution : is the position of the anchor point
        # with respect to the text, not vice-versa
        # ( rather einsteinian, isn'it )?
        
        pos_tags = ( ('se', 'e', 'ne'),
                     ('s', 'c', 'n'),
                     ('sw', 'w', 'nw' ))

        self.create_text(POSCTL_TEXT_X, POSCTL_TEXT_Y,
                         anchor='c', justify='center',
                         text='Text Position',
                         font = 'Times 18' )
        
        for r in range(0,3):
            x = POSCTL_X + (r-1)*BOX_LENGTH
            for c in range(0,3):
                y = POSCTL_Y +(c-1)*BOX_LENGTH 
                self.create_rectangle(
                    x-0.5*BOX_LENGTH, y-0.5*BOX_LENGTH,
                    x+0.5*BOX_LENGTH, y+0.5*BOX_LENGTH,
                    fill=BOX_COLOR, outline='black',
                    tag = ('posbox',pos_tags[r][c]) )


        x,y = POSCTL_X, POSCTL_Y
        self.pos_box = self.create_rectangle(x-3,y-3,x+3,y+3,
                                             fill='red',outline='black' )
        self.tag_bind('posbox', '<Any-Enter>', self.enter_callback )
        self.tag_bind('posbox', '<Any-Leave>', self.leave_callback )
        self.tag_bind('posbox', '<1>',self.setanchor_callback)


    def enter_callback( self, event ):
        self.itemconfigure('current', fill=BOX_SELECTED_COLOR )


    def leave_callback( self, event ):
        self.itemconfigure('current', fill=BOX_COLOR )


    def setanchor_callback(self, event ):
        id, = self.find_withtag('current')
        tags = self.gettags('current')
        for t in tags:
            if not t in ('current','posbox'):
                self.itemconfigure(self.text.id, anchor=t )

        # move the box indicating the current position
        x1,y1,x2,y2 = self.coords(id)
        x,y = (x1+x2)/2, (y1+y2)/2
        self.coords(self.pos_box, x-3,y-3,x+3,y+3 )


    def setjustify_callback(self, event ):
        tags = self.gettags('current')
        for t in tags:
            if not t in ('current','jbox'):
                self.itemconfigure(self.text.id, justify=t )


class CanvasTextDemo(DemoWindow):

    def __init__(self):
        l = """
        This window displays a string of text to demonstrate the text
        facilities of canvas widgets.  You can click in the boxes to
        adjust the position of the text relative to its positioning
        point or change its justification.  The text also supports
        the following simple bindings for editing:
        1. You can point, click, and type.
        2. You can also select with button 1.
        3. You can copy the selection to the mouse position with button 2.
        4. Backspace and Control+h delete the selection if there is one;
           otherwise they delete the character just before the insertion
           cursor.
        5. Delete deletes the selection if there is one; otherwise it deletes
           the character just after the insertion cursor.
        """
        DemoWindow.__init__(self,l, demo_path('ctext.py') )
        self.canvas = TextDemoCanvas(self)
        self.canvas.pack(fill=BOTH, expand=Y)


runDemo = CanvasTextDemo

## ----------------------------------------------------------------------------

if __name__ == '__main__':
    demo = CanvasTextDemo()
    mainloop()

