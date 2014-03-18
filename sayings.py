from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow

sayings = (
    "Waste not, want not",
    "Early to bed and early to rise makes a man healthy, wealthy, and wise",
    "Ask not what your country can do for you, ask what you can do for your country",
    "I shall return", "NOT",
    "A picture is worth a thousand words",
    "User interfaces are hard to build",
    "Thou shalt not steal",
    "A penny for your thoughts",
    "Fool me once, shame on you;  fool me twice, shame on me",
    "Every cloud has a silver lining",
    "Where there's smoke there's fire",
    "It takes one to know one",
    "Curiosity killed the cat",
    "Take this job and shove it",
    "Up a creek without a paddle",
    "I'm mad as hell and I'm not going to take it any more",
    "An apple a day keeps the doctor away",
    "Don't look a gift horse in the mouth"
)


class SayingsDemo(DemoWindow):

    def __init__(self):
        l="""The listbox below contains a collection of well-known sayings.
        You can scan the list using either of the scrollbars or by dragging
        in the listbox window with button 2 pressed.
        """
            
        DemoWindow.__init__(self, l, 'sayings.py' )

        # create the list
        frame = Frame(self); frame.pack(expand=YES, fill=Y)
        list = Listbox(frame,  setgrid=1)
        vbar = Scrollbar(frame,command=list.yview)
        list['yscrollcommand'] = vbar.set
        hbar = Scrollbar(frame,command=list.xview,orient='horizontal')
        list['xscrollcommand'] = hbar.set

        #pack all toghether
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0,weight=1)
        list.grid(row=0,column=0,sticky='nsew')
        vbar.grid(row=0,column=1,sticky='ns')
        hbar.grid(row=1,column=0,sticky='ew')
        

        # fill the list
        for i in sayings:
            list.insert(END,i)


        
runDemo = SayingsDemo        

if __name__ == '__main__':
    demo = SayingsDemo()
    mainloop()

