
from tkinter import *
from tkinter.ttk import *

import infrastructure


class CheckbuttonsDemoWindow( infrastructure.DemoWindow ):
    """
    A demo window with two set of checkbuttons, each related to
    a different variable. A pop-up window allows to show the
    values of these variables.
    """
    
    def __init__( self ):
        intro="""Three checkbuttons are displayed below.
        If you click on a button, it will toggle the button\'s selection
        state and set a Variable object to a value indicating the state of
        the checkbutton. Click the 'See Variables' button to see the
        current values of the variables.
        """
             
        infrastructure.DemoWindow.__init__(self, intro, 'check.py' )

        self.frame=Frame(self)
        self.frame.pack(expand=YES, fill=BOTH )
        self.vars = []
        for c in ('Wipers OK',
                  'Brakes OK',
                  'Driver Sober' ):
            v = IntVar(self)
            b = Checkbutton(self.frame, text=c, variable=v)
            self.vars.append( (v,c) )
            
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
        for v,name in self.vars :
            ln=Label(frame, text=name+':')
            ln.grid(row=cnt,column=0)
            lv = Label(frame, text=str(v.get()) )
            lv.grid(row=cnt,column=1)
            cnt=cnt+1

        b=Button(top, text='Dismiss', command=top.destroy )
        b.pack( side=BOTTOM, expand=YES )



runDemo = CheckbuttonsDemoWindow

if __name__ == '__main__' :
    demo = CheckbuttonsDemoWindow()
    mainloop()

