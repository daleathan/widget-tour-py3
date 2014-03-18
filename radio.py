# ---
# radio.py
#
# A demo window showing how to use radio-bttons
#

from tkinter import *
from tkinter.ttk import *

import infrastructure


class RadiobuttonsDemoWindow( infrastructure.DemoWindow ):
    """
    A demo window with some radio buttons, connected with variable
    objects. A pop-up window shows variable values
    """
    def __init__( self ):
        intro = """Two groups of radiobuttons are displayed below.
        If you click on a button then the button will become selected
        exclusively among all the buttons in its group.  A  variable
        object is associated with each group to indicate which of the group's
        buttons is selected.  Click the \"See Variables\" button to see
        the current values of the variables."""
             
        infrastructure.DemoWindow.__init__(self, intro, 'radio.py' )

        self.frame=Frame(self)
        self.frame.pack(expand=YES, fill=BOTH )

        # create the column of point sizes
        left_f = Frame(self.frame)
        left_f.pack(side=LEFT, expand=YES, fill=X)
        self.size_var = IntVar(self)
        for c in (12, 18,24):
            b = Radiobutton(left_f, text="Point Size "+str(c),
                            variable=self.size_var, value=c)
            b.pack( side=TOP, expand=YES, pady=2, anchor='w' )

        # create the column of colors
        right_f = Frame(self.frame)
        right_f.pack(side=RIGHT, expand=YES, fill=X)
        self.color_var=StringVar(self)
        for c in ('red','green','blue','yellow','orange', 'purple' ):
            b = Radiobutton(right_f, text=c,
                            variable=self.color_var, value=c)
            b.pack( side=TOP, expand=YES, pady=2, anchor='w' )

        button = Button(self, text='See variables',
                        command=self.callback )
        button.pack(side=TOP, expand=YES)

        
    def callback(self):
        # show the current variable values in a value
        top = Toplevel()
        top.title('Variable values')
        l = Label(top, text='Variable values:', font=('Helvetica', 18 ))
        l.pack(side=TOP, pady=5)
        frame = Frame(top)
        frame.pack(side=TOP, expand=YES, fill=BOTH)
        frame.columnconfigure(0, minsize=200)
        cnt=0

        
        r1 = 'Point size = %d' % self.size_var.get()
        r2 = 'color = %s' % self.color_var.get()
        for r in r1,r2 :
            Label(frame, text=r ).pack(side=TOP, pady=4)

        b=Button(top, text='Dismiss', command=top.destroy )
        b.pack( side=BOTTOM, expand=YES )

        

runDemo = RadiobuttonsDemoWindow

if __name__ == '__main__' :
    demo = RadiobuttonsDemoWindow()
    mainloop()

