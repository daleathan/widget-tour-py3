##
# --- menu.py
# A demo of menus using python/tk
#

from tkinter import *

import tkMessageBox
import tkSimpleDialog

from infrastructure import DemoWindow, demo_path, callit

import sys
if sys.platform != 'macos':
    POST_KEY ='Alt'
    ACCEL_KEY='Meta' 
else:
    POST_KEY='Command'
    ACCEL_KEY='Command'
    

class ShowvarsDialog(tkSimpleDialog.Dialog):
    "A dialog to show values of a set of variables"
    def __init__(self, parent, pairs):
        self.pairs=pairs
        tkSimpleDialog.Dialog.__init__(self, parent)
            
    def body(self, body): # overrides parent class hook
        self.frame= body
        for name,value in self.pairs:
            l = Label( self.frame, text='%s = %s'% (name, value) )
            l.pack(side=TOP,expand=Y,fill=X)
        
    def buttonbox(self):
        """overrides parent method - only the dismiss
        button is needed"""
        
        box = Frame(self, border=2, relief=SUNKEN)

        w = Button(box, text="dismiss", width=10, command=self.cancel)
        w.pack(side=LEFT, expand=Y, fill=X)

        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)

        box.pack(fill=X,expand=YES, side=BOTTOM)


class MenuDemo( DemoWindow ):

    def __init__(self):

        l = ("""This window contains a menubar with cascaded menus.
        You can post a menu from the keyboard by typing %s+x,
        where \"x\" is the character underlined on the menu.
        You can then traverse among the menus using the arrow keys.
        When a menu is posted, you can invoke the current entry by
        typing space, or you can invoke any entry by typing its
        underlined character.  If a menu entry has an accelerator,
        you can invoke the entry without posting the menu just by
        typing the accelerator. The rightmost menu can be torn
        off into a palette by selecting the first item in the menu.
        """ % POST_KEY )
        DemoWindow.__init__(self,l, demo_path('menu.py'))


    def hook_create_menubar(self):

        self.mbar = Menu(self, type='menubar')
        self['menu'] = self.mbar

        # create the 'File' menu
        menu = Menu(self.mbar, tearoff=0)
        self.mbar.add_cascade(label='File', underline=0, menu=menu )
        menu.add_command(label='0pen...', underline=0,
                         command=callit(self.dummy_callback,'Open'))
        menu.add_command(label='New', underline=0,
                         command=callit(self.dummy_callback,'New'))
        menu.add_command(label='Save', underline=0,
                         command=callit(self.dummy_callback,'Save'))
        menu.add_command(label='Save As ...', underline=5,
                         command=callit(self.dummy_callback,'Save As'))
        menu.add_separator()
        menu.add_command(label='Print', underline=0,
                         command=callit(self.dummy_callback,'Print'))
        menu.add_command(label='Print Setup ...', underline=5,
                         command=callit(self.dummy_callback,'Print Setup'))
        menu.add_separator()
        menu.add_command(label='Dismiss', underline=0,
                         command=self.dismiss_callback)


        # create the basic menu
        menu = Menu(self.mbar, tearoff=0 )
        self.mbar.add_cascade(label='Basic', underline=0, menu=menu)        
        menu.add_command(label='Long entry which does nothing')
        for l in ('A','B','C','D','E', 'F'):
            menu.add_command(label='Print letter "%s"'%l,
                             accelerator='%s+%s'%(ACCEL_KEY,l),
                             command=callit(self.printletter_callback, l ))
        
        # create the 'Cascades' menu
        menu = Menu(self.mbar, tearoff=0 )
        self.mbar.add_cascade(label='Cascades', underline=0, menu=menu)
        menu.add_command(label='Print Hello',
                         accelerator='%s+%s'%(ACCEL_KEY,'H'),
                         command=callit(self.print_callback, "Hello!"))
        menu.add_command(label='Print Goodby',
                         accelerator='%s+%s'%(ACCEL_KEY,'G'),
                         command=callit(self.print_callback, "Goodby!"))



        # add check buttons sub-menu
        cb_menu = Menu(menu,tearoff=0)
        self.vars={}
        labels = ('Oil checked', 'Transmission checked',
                  'Brakes checked', 'Lights checked' )
        for l in labels:
            self.vars[l]=IntVar(self)
            cb_menu.add_checkbutton(label=l,
                                    variable=self.vars[l] )
        cb_menu.add_separator()
        cb_menu.add_command(label='Show variables',
                            command=callit(self.showvars_callback,
                                           labels ) )
        menu.add_cascade(label='Check buttons', underline=0,
                         menu=cb_menu)

        # add radio-buttons sub-menu
        cb_menu=Menu(menu,tearoff=0)
        self.vars['size'] = StringVar(self)
        self.vars['font'] = StringVar(self)
        for l in (10,14,18,24,32):
              cb_menu.add_radiobutton(label=`l`+' points',
                                      variable=self.vars['size'] )
        cb_menu.add_separator()
        for l in ('Roman','Bold','Italic'):
              cb_menu.add_radiobutton(label=l,
                                      variable=self.vars['font'] )
        cb_menu.add_separator()
        cb_menu.add_command(label='Show variables',
                            command=callit(self.showvars_callback,
                                           ('size', 'font') ))
        menu.add_cascade(label='Radio buttons', underline=0,
                         menu=cb_menu)

        # add 'Icons' menu
        menu = Menu(self.mbar, tearoff=0)
        self.mbar.add_cascade(label='Icons', underline=0, menu=menu)
        for b in ( '@'+demo_path('images','pattern.bmp'),
                   'info', 'questhead', 'error' ):
            menu.add_command(bitmap=b, hidemargin=1,
                           command=self.icon_callback )
        menu.entryconfigure(2,columnbreak=1)
                           

        # add 'More' menu
        menu = Menu(self.mbar, tearoff=0)
        self.mbar.add_cascade(label='More', underline=0, menu=menu)
        for l in ( 'An entry', 'Another entry', 'Does nothing',
                   'Just turn thumbs' , 'Save the world',
                   'Armageddon'):
            menu.add_command(label=l,
                             command=callit(self.youselected_callback,l))
        

        # And, finally, add the colors menu
        menu = Menu(self.mbar, tearoff=1)
        self.mbar.add_cascade(label='Colors', underline=2, menu=menu)
        for l in ( 'red','green', 'blue', 'yellow', 'cyan', 'orange', 'brown'):
            menu.add_command(label=l,
                             background=l,
                             command=callit(self.color_callback,l))


        # bind menu entry selection event
        # ?? Why it does not work for Menubuton selection ??
        # (the tk demo does it)
        self.bind_class('Menu', '<<MenuSelect>>', self.entryselect_callback )
        self.bind_class('Menubutton', '<<MenuSelect>>', self.entryselect_callback )

    def hook_create_statusline(self):
        self.frame_statusline = Frame(self,relief=SUNKEN,border=2)
        self.frame_statusline.pack(side=BOTTOM,expand=Y, fill=BOTH)
        self.statusline = Label(self.frame_statusline, justify=LEFT)
        self.statusline.pack(side=LEFT )

    #
    # --- callbacks
    #

    def dummy_callback(self, option):
        msg = (
           "This is just a demo: no action has been defined for the %s entry"
           % option )
        tkMessageBox.showwarning(title='Not Implemented', message=msg )


    def entryselect_callback (self,event):
        try :
            l = self.tk.eval('%s entrycget active -label' % event.widget )
        except TclError: l=None # the selected item has no label
        if l:
            self.statusline.configure({'text':l, 'justify':'left'})


    def printletter_callback(self, l):
        tkMessageBox.showinfo(title='Printed letter',
                                 message='You printed letter: "%s"' % l )


    def print_callback(self, l):
        tkMessageBox.showinfo(title='Print',
                                 message= l )

    def showvars_callback(self, names):
        pairs=[]
        for n in names:
            pair = (n, str(self.vars[n].get()) )
            pairs.append( pair )
        dlg = ShowvarsDialog(self,pairs)        

    def icon_callback(self):
        tkMessageBox.showinfo(
            title='Selected Icon',
            message= ("The menu entry you invoked displays"+
                      " a bitmap rather than a text string."+
                      "Other than this, it is just like any "+
                      "other menu entry." )
            )

    def youselected_callback(self, l):
        tkMessageBox.showinfo(
            title='You selected',
            message = 'You selected : '+l )

    def color_callback(self,c):
        self.statusline['background']=c
        self.frame_statusline['background']=c


runDemo = MenuDemo

## ----------------------------------------------------------------------------

if __name__== '__main__':
    demo = MenuDemo()
    mainloop()
    





