
from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow


class EntryDemoWindow(DemoWindow):

    def __init__(self):
        l = """hree different entries are displayed below.
        You can add characters by pointing, clicking and typing.
        The normal Motif editing characters are supported, along with many
        Emacs bindings.  For example, Backspace and Control-h delete the
        character to the left of the insertion cursor and Delete and
        Control-d delete the chararacter to the right of the insertion cursor.
        For entries that are too large to fit in the window all at once,
        you can scan through the entries by dragging with mouse button2
        pressed.
        """
        DemoWindow.__init__(self, l, 'entry1.py' )

        frame = Frame(self); frame.pack(expand=YES, fill=BOTH)
        w1 = Entry(frame)
        w2 = Entry(frame)
        w3 = Entry(frame)
        for w in w1,w2,w3:
            w.pack(side=TOP, fill=X,padx=5, pady=10 )

        w1.insert(0, 'Initial value')

        w2.insert(0,"This entry contains a value much too long ")
        w2.insert(END,"to fit in the window at one time, so long in fact")
        w2.insert(END," that you will have to scroll or scan to see the end.")


runDemo = EntryDemoWindow


if __name__ == '__main__':
    demo = EntryDemoWindow()
    mainloop()

