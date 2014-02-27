# --- button.py
# This module demonstrates simple buttons
# It is meant to be called by the demo widget main module
# but it can also run stand-alone
#

from Tkinter import *

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

        ## BUG!
        ## This is the syntax error which causes Python 1.6 to crash.
        ## Removing the error, the crash does not happen anymore.
        ## the correct line should be
        ## infrastructure.DemoWindow.__init__(self, intro, 'buttons.py')
        infrastructure.DemoWindow(self, intro )

        frame=Frame()
        frame.pack(expand=YES, fill=BOTH )
        for c in ('Peach Puff', 'Light Blue1',
                  'Sea Green2', 'Yellow1' ):
            b = Button(self, text=c)
            b['command'] = callit( self.callback, c );
            
            b.pack( side=top, expand=yes, pady=2,
                    command=callit(self.callback, color) )

    def callback(self, color):
        self.frame['background']=color
            


if __name__ == '__main__':
    infrastructure.rundemo('ButtonsDemoWindow', locals(), globals())    
    mainloop()
