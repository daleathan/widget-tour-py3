from tkinter import *

from infrastructure import *


class ImageDemoWindow(DemoWindow):

    def __init__(self):
        l="""This demonstration displays two images, each in
        a separate label widget.
        """

        DemoWindow.__init__(self,l, 'image1.py')

        # load the images in object attributes
        self.top_image=PhotoImage(master=self, file='images/earth.gif' )
        self.bottom_image=PhotoImage(master=self, file='images/earthris.gif' )

        # create the two labels
        frame = Frame(self); frame.pack(expand=YES, fill=BOTH)
        for img in self.top_image, self.bottom_image:
            l = Label(frame, image=img, relief=SUNKEN, bord=2 )
            l.pack(side=TOP, expand=YES, fill=X )
            

runDemo = ImageDemoWindow

if __name__ == '__main__' :
    demo = ImageDemoWindow()
    mainloop()
