
from tkinter import *
import tkSimpleDialog

from infrastructure import DemoWindow, demo_path


class MyDialog(tkSimpleDialog.Dialog):

    def __init__(self, parent, title, message, grab='local'):
        self.message=message # used in body
        self.grab = grab     # used in grab_set

        tkSimpleDialog.Dialog.__init__(self,parent,title) # this calls body


    def body(self, body_frame): # overrides parent class method
        l = Label(body_frame, text=self.message, wrap=450 )
        l.pack(expand=YES, fill=BOTH)

        # global grab cannot be set befor windows is 'viewable'
        # and this happen in mainloop after this function returns
        # Thus, it is needed to delay grab setting of an interval
        # long enough to make sure that the window has been made
        # 'viewable'
        if self.grab == 'global':
            self.after(100, self.grab_set_global )
        else:
            pass # local grab is set by parent class constructor

        

class GrabDemo(DemoWindow):

    def __init__(self):

        l="""This demo shows you two ways of having
        a dialog to grab focus: local and global grab.
        Click on the relevant button and learn about
        the differences"""

        DemoWindow.__init__(self, l, demo_path('dialoggrab.py'))

        frame=Frame(self, relief=RIDGE,border=2); frame.pack(expand=YES,fill=BOTH)
        b1=Button(frame,text='Open dialog with local grab',
                  command=self.localgrab_callback)
        b2=Button(frame,text='Open dialog with global grab',
                  command=self.globalgrab_callback)
        for b in b1,b2: b.pack(side=LEFT, padx=5)
                          

    def localgrab_callback(self):
        l=('This is a modal dialog box.  It uses Tk\'s "grab" command to'+
           'create a "local grab" on the dialog box.  The grab prevents any'+
           ' pointer-related events from getting to any other windows in the'+
           ' application until you have answered the dialog by invoking one'+
           ' of the buttons below.  However, you can still interact with'+
           ' other applications.')

        MyDialog(self, title='Dialog with local grab',
                 message=l, grab='local' )
                 
        

    def globalgrab_callback(self):
        l=('This dialog box uses a global grab, so it prevents you '+
           'from interacting with anything on your display until you ' +
           'invoke one of the buttons below.  Global grabs are almost '+
           'always a bad idea; don\'t use them unless you\'re truly desperate.'
           )
        MyDialog(self, title='Dialog with local grab',
                 message=l, grab='global' )


runDemo = GrabDemo


if __name__ == '__main__':
    demo = GrabDemo()
    mainloop()
