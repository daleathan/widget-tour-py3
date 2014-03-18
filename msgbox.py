## ----
# msgbox.py : demo of the message boxes
#

from tkinter import *
from tkinter.messagebox import Message

from infrastructure import DemoWindow, demo_path

class OptionPanel(Frame):
    "A frame with a set of radiobuttons to select an option"

    def __init__(self, master, title, *options ):
        Frame.__init__(self,master,relief='ridge', border=2)

        t=Label(self,text=title, justify='c', anchor='n')
        t.pack(side=TOP, fill=X)

        s=Frame(self, height=3, relief='ridge', border=1)
        s.pack(side=TOP, fill=X)

        self.radiovar=StringVar(self)
        for o in options:
            r = Radiobutton(self,text=o, variable=self.radiovar, value=o,
                            anchor='w')
            r.pack(side=TOP,fill=X)
    
    def get(self):
        return self.radiovar.get()

    def set(self,value):
        return self.radiovar.set(value)


class MessageBoxDemo(DemoWindow):

    def __init__( self ):
        l="""
        Choose the icon and type option of the message box.
        Then press the \"Message Box\" button to see the message box.
        """
        DemoWindow.__init__(self,l,demo_path('msgbox.py'))

        frame=Frame(self);frame.pack(expand=Y, fill=BOTH)

        #create the two option panels
        middleframe=Frame(frame); middleframe.pack(side=TOP,fill=X)
        p1 = OptionPanel(middleframe,'Icon',
                         'error', 'window', 'question', 'warning')
        p1.set('error')
        p1.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        p2 = OptionPanel(middleframe,'Type',
                         'abortretryignore', 'ok', 'okcancel',
                         'retrycancel', 'yesno' )
        p2.set('ok')
        p2.pack(side=RIGHT, expand=YES, fill=BOTH, padx=10,pady=10)

        b = Button(frame,text='Open Dialog', command=self.opendialog_callback )
        b.pack(side=TOP,fill=X, padx=10)
        
        self.p1, self.p2 = p1,p2 # needed by the callback

    def opendialog_callback(self):
        msg=( 'This is a message box of type %s, widh icon %s' %
              (self.p2.get(), self.p1.get() ))

        # Note : the dialog is modal, and returs the pressed button
        dlg=Message( title='MessageBox',message=msg, parent=self,
                 icon=self.p1.get(), type=self.p2.get() )
        selection = dlg.show()
        Message(
            parent=self, icon='info', type='ok',
            title='Your Choice', message='You pressed '+selection ).show()
        

runDemo = MessageBoxDemo

## ----------------------------------------------------------------------------
if __name__ == '__main__':
    demo=MessageBoxDemo()
    mainloop()

