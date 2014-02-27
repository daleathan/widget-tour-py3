
from tkinter import *

from infrastructure import *

class BitmapButtonsDemo ( DemoWindow ):

    def __init__(self):
        l = """This window shows three ways of using bitmaps or images
        in radiobuttons and checkbuttons.  On the left are two radiobuttons,
        each of which displays a bitmap and an indicator.
        In the middle is a checkbutton that displays a different image
        depending on whether it is selected or not.
        On the right is a checkbutton that displays a single
        bitmap but changes its background color to indicate
        whether or not it is selected."""

        DemoWindow.__init__(self, l, 'iconbuttons.py' )

        frame = Frame(self); frame.pack( side=TOP, expand=YES, fill=BOTH )
        f_left = Frame(frame); f_left.pack(side=LEFT, expand=YES, fill=BOTH);
        self.radiovar=StringVar(f_left).set('No letters');

        #
        # Images shall be assigned to object attributes or they are
        # garbage collected before time. This results in an error like
        # 'bitmap does not exist' (if you ue directly bitmap=BitmapImage(...)
        # or in the image simply not being displayed (if you use a local
        # variable ).
        #
        self.letters = BitmapImage(master=self,file='images/letters.bmp')
        self.noletter = BitmapImage(master=self,file='images/noletter.bmp')
        self.flagdown = BitmapImage(master=self,file='images/flagdown.bmp')
        self.flagup = BitmapImage(master=self,file='images/flagup.bmp')
    
        
        rb1 = Radiobutton(f_left,
                          image=self.letters,
                          variable=self.radiovar,
                          value='There are letters')
        rb2 = Radiobutton(f_left,
                          image=self.noletter,
                          variable=self.radiovar,
                          value='No letters')
        for r in rb1,rb2:
            r.pack(side=TOP, expand=YES)

        cb = Checkbutton(frame, image=self.flagdown,
                         selectimage=self.flagup,
                         indicatoron=0 ) 
        cb['selectcolor']=cb['background'] # otherwise is red(default)
        cb2 = Checkbutton(frame, image=self.letters,
                          selectcolor='lightgreen',
                          indicatoron=0 )
        for b in cb,cb2:
            b.pack(side=LEFT, expand=YES)


runDemo = BitmapButtonsDemo

if __name__ == '__main__' :
    demo = BitmapButtonsDemo()
    mainloop()
