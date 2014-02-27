# label.py --
#
# This demonstration program creates a toplevel window containing
# several label widgets.
#

from tkinter import *

# import common used utilities
import infrastructure

    
class LabelDemoWindow( infrastructure.DemoWindow ):
    """
    This is the main window of the demo label.
    It shows 5 labels : one which explains the demo,
    one plain label, one sunken, one raised, and
    finally one image label.
    """
    
    def __init__( self ):

        l_text ="""Five labels are displayed below:
           three textual ones on the left,and an image
           label and a text label on the right.
           Labels are pretty boring because you can't
           do anything with them.
           """
        infrastructure.DemoWindow.__init__(self, l_text, 'label.py')

        frame = Frame(self)
        frame.pack(expand=YES, fill=BOTH)
        # creates and pack the three textual  labels
        l1 = Label(frame, text='First Label')
        l2 = Label(frame, text='Second label, raised', relief=RAISED )
        l3 = Label(frame, text='Third label, sunken', relief=SUNKEN )
        for l in (l1, l2, l3):
            l.pack(side=TOP, expand=YES, pady=2, anchor='w' )

        # the original demo has bitmaps here, but images are more fun.
        # which other kind of images are supported, beside 'gif?'
        
        # you need to store the PhotoImage object in an attribute, otherwise
        # it is garbage collected and its __delete__ method deletes the
        # Tk image, too !!
        self.image = PhotoImage(master=self, file='images/village.gif')
        bitmap = Label(self, image=self.image, relief=SUNKEN, borderwidth=2)
        caption = Label(self, text='My home village' )
        for l in bitmap,caption :
            l.pack(side=TOP, anchor='e')
      


# this is the entry point fow widget.py
def runDemo():
    LabelDemoWindow()


# ============================================================================
# module self-test code


if __name__ == '__main__':
    LabelDemoWindow()
    mainloop()

    


