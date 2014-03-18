# --- button.py
# This module demonstrates simple buttons
# It is meant to be called by the demo widget main module
# but it can also run stand-alone
#

from tkinter import *
from tkinter.ttk import *

# common code used by all demo modules
import infrastructure


class ButtonsDemoWindow( infrastructure.DemoWindow ):
    """
    A demo window with some buttons which changes the demo
    window behaviour
    """
    def __init__( self ):
        intro="""If you click on any of the four buttons below, the background
        of the button area will change to the color indicated in the button.
        You can press Tab to move among the buttons, then press Space to
        invoke the current button."""

        
        infrastructure.DemoWindow.__init__(self, intro, 'button.py' )

        self.frame=Frame(self)
        self.frame.pack(expand=YES, fill=BOTH )
        for c in ('Peach Puff', 'Light Blue',
                  'Sea Green', 'Yellow' ):
            b = Button(self.frame, text=c)
            b['command'] = infrastructure.callit( self.callback, c );
            
            b.pack( side=TOP, expand=YES, pady=2 )
            

    def callback(self, color):
        self.frame['background']=color
            

def runDemo():
    ButtonsDemoWindow()
    

if __name__ == '__main__':
    demo = ButtonsDemoWindow()
    demo.mainloop()

