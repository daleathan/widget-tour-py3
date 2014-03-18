
from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow

# For some reason, the 'xview' method of Entry class does not work
# like the 'xview' methods of other widgets. It accepts only an 'index'
# argument, instead of the usual variable-lebgth list.
# Therefore, doing the usual scrollbar['command']=entry.xview generates
# an error (wrong number of arguments) every time the scrollbar is
# moved.
# To bypass this, I created my own subclass of Entry widget,
# to which I added an 'xview2' method, which I can use instead od xview
#

class MyEntry( Entry ):
    def __init__(self, master=None):
        Entry.__init__(self, master)

    def xview2(self, *what):
        if not what:
            return self._getdoubles(self.tk.call(self._w, 'xview'))
        self.tk.call((self._w, 'xview') + what)

        

class ScrolledEntryDemoWindow(DemoWindow):

    def __init__(self):
        l = """Three different entries are displayed below, with a
        scrollbar for each entry.  You can add characters by pointing,
        clicking and typing.  The normal Motif editing characters are
        supported, along with many Emacs bindings.  For example,
        Backspace and Control-h delete the character to the left of
        the insertion cursor and Delete and Control-d delete the
        chararacter to the right of the insertion cursor.
        For entries that are too large to fit in the window all at
        once, you can scan through the entries with the scrollbars,
        or by dragging with mouse button2 pressed."""
        
        DemoWindow.__init__(self, l, 'entry2.py' )


        frame = Frame(self); frame.pack(expand=YES, fill=BOTH)

        f1,w1,sbar1 = self.create_scrollable_entry(frame)
        f2,w2,sbar2 = self.create_scrollable_entry(frame)
        f3,w3,sbar3 = self.create_scrollable_entry(frame)
        
        for f in f1,f2,f3:
            f.pack(side=TOP, expand=Y, fill=X,padx=5, pady=10 )

        w1.insert(0, 'Initial value')

        w2.insert(0,"This entry contains a value much too long ")
        w2.insert(END,"to fit in the window at one time, so long in fact")
        w2.insert(END," that you will have to scroll or scan to see the end.")

        
    def create_scrollable_entry(self, master):
        """This routine creates a frame with inside an entry and
        a connected horizontal scroll bar"""
        f = Frame(master)
        e = MyEntry(f)
        sbar = Scrollbar(f, orient='horiz' )

        e.pack(side=TOP, expand=Y, fill=X )
        sbar.pack(side=TOP, expand=Y, fill=X )

        sbar['command'] = e.xview2 # xview does not work. See comments before
        e['xscrollcommand'] = sbar.set

        
        return f,e,sbar


runDemo = ScrolledEntryDemoWindow

if __name__ == '__main__':
    demo = ScrolledEntryDemoWindow()
    mainloop()

