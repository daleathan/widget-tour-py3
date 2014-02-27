##
# --- filebox.py
# Demo of python/tk file dialogs
#
from tkinter import *
from tkinter import filedialog 

from infrastructure import DemoWindow, demo_path

class FileDialogDemo(DemoWindow):

    def __init__(self):
        l="""Enter a file name in the entry box or click on the
        \"Browse\" buttons to select a file name using the file
        selection dialog."""

        DemoWindow.__init__(self, l, demo_path('filebox.py') )

        frame = Frame(self); frame.pack(side=TOP,expand=YES,fill=BOTH)

        l1 = Label(frame, text='Select a file to open:')
        l2 = Label(frame, text='Select a file to save:')
        e1=Entry(frame); self.e1=e1
        e2=Entry(frame); self.e2=e2
        b1 = Button(frame, text='Browse...', command=self.selectopen_callback)
        b2 = Button(frame, text='Browse...', command=self.selectsave_callback)

        frame.rowconfigure(1,pad=10, weight=1)
        for r in (0,1,2):
            frame.columnconfigure(r, pad=5)

        # insert elements in the container
        rnum=0
        for r in ( (l1, e1, b1), (l2, e2, b2) ):
            cnum=0
            for w in r :
                w.grid(row=rnum, column=cnum ) 
                cnum=cnum+1
            rnum=rnum+1

        self.mvar=IntVar(self)
        mb = Checkbutton(self, text='Use motif stile dialog',
                         variable=self.mvar, command=self.changestyle_callback )
        mb.pack(side=TOP, expand=YES, fill=X )

    def changestyle_callback(self):
        self.tk_strictMotif(self.mvar.get())

    def selectopen_callback(self):
        f = filedialog.askopenfilename()
        self.e1.delete(0,END); self.e1.insert(0,f)

    def selectsave_callback(self):
        f = filedialog.asksaveasfilename()
        self.e2.delete(0,END); self.e2.insert(0,f)        



runDemo = FileDialogDemo

if __name__ == '__main__':
    demo = FileDialogDemo()
    mainloop()
    
