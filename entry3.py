
from tkinter import *

from infrastructure import DemoWindow



class FormEntryDemo (DemoWindow ):
    def __init__(self):
        l="""This window contains a simple form where you can type in
        the various entries and use tabs to move circularly between
        the entries."""

        DemoWindow.__init__(self, l, 'entry3.py')

        frame = Frame(self);frame.pack( expand=YES, fill=X)

        for text in ('Name:', 'Address:', '', '', 'Phone' ):
            f = Frame(frame, bd=2 );
            f.pack(side=TOP, fill=X )
            l = Label( f, text=text );
            l.pack(side=LEFT)
            e = Entry(f, relief=SUNKEN, border=2, width=40 );
            e.pack(side=RIGHT)
            


runDemo = FormEntryDemo

if __name__ == '__main__':
    demo = FormEntryDemo()
    mainloop()
