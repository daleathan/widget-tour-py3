
from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow, demo_path


class BuiltinBitmapsDemo(DemoWindow):

    def __init__(self):

        l="""This window displays all of Tk's built-in bitmaps,
        along with the names you can use for them in  scripts.
        """

        DemoWindow.__init__(self,l, demo_path('bitmap.py'))

        frame=Frame(self);frame.pack(expand=YES, fill=BOTH, pady=10)

        list=( 'error', 'gray12', 'gray25', 'gray50', 'gray75',
               'hourglass', 'info', 'question', 'questhead', 'warning' )

        row=0; column=0
        for b in list:
            f = Frame(frame)
            l1=Label(f, bitmap=b ); l1.pack(side=TOP)
            l2=Label(f, text=b);l2.pack(side=BOTTOM)
            f.grid(row=row, column=column, sticky='ns', padx=10 )
            column=column+1;
            if column >= len(list)/2:
                row=row+1
                column=0

def runDemo():
    demo=BuiltinBitmapsDemo()

    

if __name__ == '__main__':
    demo=BuiltinBitmapsDemo()
    mainloop()

