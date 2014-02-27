##
# --- colorchooser.py
# How to use the color dialog callback with python/tk
#

from tkinter import *
import tkColorChooser

from infrastructure import DemoWindow, demo_path

class ColorChooserDemo(DemoWindow):

    def __init__(self):
        l = """Press the buttons below to choose the foreground and
        background colors for the widgets in this window."""

        DemoWindow.__init__(self,l,demo_path('colorchooser.py'))

        frame=Frame(self); frame.pack(expand=YES, fill=BOTH)
        button_fg = Button(frame, text='Foreground',
                                command=self.fg_callback  )
        button_bg = Button(frame, text='Background',
                                command=self.bg_callback )
        for b in button_fg,button_bg:
            b.pack(side=TOP, padx=10, pady=5, expand=YES, fill=X )

        self.all_widgets = ( frame, button_fg, button_bg )

    def all_subwidgets(self):
        "It flattens the widget hierarchy in a single list"
        l = self.children.values ()
        cnt = 0
        while cnt < len(l):
            l = l+l[cnt].children.values()
            cnt=cnt+1
        return l
                
            
        
    def fg_callback(self):

        rgb, color = tkColorChooser.askcolor(self.all_widgets[1]['foreground'])
        if color:
            for w in [self,]+self.all_subwidgets():
                try:
                    w['foreground']= color
                except TclError:pass # child may not have 'foreground' prop.


    def bg_callback(self):

        rgb, color = tkColorChooser.askcolor(self.all_widgets[0]['background'])
        if color:
            for w in [self,]+self.all_subwidgets():
                try:
                    w['background']= color
                except TclError: pass # child may not have 'background'



if __name__ == '__main__':
    demo = ColorChooserDemo()
    mainloop()

                
