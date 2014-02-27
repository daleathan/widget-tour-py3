
from Tkinter import *
import infrastructure

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##
## Never mix two 'packing styles!
##
## As you can see in this example, the 'packing manager' gets
## connfused and locks in a CPU-connsuming never-ending loop
##
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class CheckbuttonsDemoWindow( infrastructure.DemoWindow ):
    """
    A demo window with some buttons which changes the demo
    window behaviour
    """
    def __init__( self ):
        intro="""Three checkbuttons are displayed below.
        If you click on a button, it will toggle the button\'s selection
        state and set a Perl variable to a value indicating the state of
        the checkbutton. Click the 'See Variables' button to see the
        current values of the variables.
        """
             
        infrastructure.DemoWindow.__init__(self, intro, 'buttons.py' )

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


## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Here is the problem. The window created in 'callback' method
## uses both 'grid' and 'pack' layout manager function
## You can see the result when clicking 'see variable' button of the main
## window. Be ready to kill the process, first.
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
    def callback(self):
        # show the current variable values in a value
        top = Toplevel()
        cnt=0
        for v,name in self.vars:

            ln=Label(top, text=name+':')
            ln.grid(row=cnt,column=0)
            lv = Label(top, text=str(v.get()) )
            lv.grid(row=cnt,column=1)
            cnt=cnt+1

        b=Button(top, text='Dismiss', command=top.destroy )
        b.pack( side=BOTTOM, expand=YES )

        

if __name__ == '__main__' :
    demo = CheckbuttonsDemoWindow()
    mainloop()



