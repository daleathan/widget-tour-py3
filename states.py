
from tkinter import *

from infrastructure import DemoWindow
from common import HScrollList

class StatesDemo(DemoWindow):

    states=( 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
         'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
         'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
         'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
         'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
         'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
         'New Mexico', 'New York', 'North Carolina', 'North Dakota',
         'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', "Rhode Island",
         "South Carolina", "South Dakota", 'Tennessee', 'Texas', 'Utah',
         'Vermont', 'Virginia', 'Washington', "West Virginia", 'Wisconsin',
         'Wyoming'  )

    def __init__(self):
        l="""A listbox containing the 50 states is displayed below,
        along with a scrollbar.  You can scan the list either using
        the scrollbar or by scanning.  To scan, press button 2 in
        the widget and drag up or down."""
    
        DemoWindow.__init__(self, l, 'states.py' )

        # create the list
        self.list=HScrollList(self)
        self.list.pack(expand=YES, fill=Y )

        # scroll the list
        for i in StatesDemo.states:
            self.list.list.insert(END,i)



runDemo = StatesDemo

if __name__ == '__main__':
    demo = StatesDemo()
    mainloop()



