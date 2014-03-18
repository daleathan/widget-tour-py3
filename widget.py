#
# The 'main module' of the widget-demo 
#
from tkinter import *
from tkinter import ttk

import sys
import os

from infrastructure import *
from common import *

#needed by canvasruler
TOPLEVEL_TK = None


#
# 
# This table contains the list of demos (description, module name )
# The elements with a null file name are section headers
# NOTE : modules shall have names compatible with identifier name rules
#
demos = [ ("Labels, buttons, checkbuttons, and radiobuttons", None ),
          ('Labels (text and bitmaps)', 'label' ),
          ('Labels and UNICODE text(TBD)', 'unicodeout' ),
          ('Buttons', 'button' ),
          ('Check-buttons(select any of a group)','check'),
          ('Radio-buttons(select one of a group)','radio'),
          ('A 15-puzzle game made out of buttons','puzzle'),
          ('Iconic buttons that use bitmaps','icon'),
          ('Two labels displaying image','image1'),
          ('A simple user interface for viewing images','image2'),
          ('Labelled frames(TBD)', 'labelframe' ),
          ('The simple Themed Tk widgets(TBD)', 'ttkbut' ),
          
          ('Listboxes and Trees', None ),
          ('The 50 USA states', 'states' ),
          ('Colors:change the color scheme for the application', 'colors'),
          ('A collection of famous and infamous sayings', 'sayings' ),
          ('A multi-column list of countries(TBD)', 'mclist' ),
          ('A directory browser tree(TBD)', 'tree' ),
          
          ('Entries, Spin-boxes and Combo-boxes', None ),
          ('Entries without scrollbars', 'entry1' ),
          ('Entries with scrollbars', 'entry2' ),
          ('Validated entries and password fields(TBD)', 'entry3' ),
          ('Spin-boxes(TBD)', 'spin' ),
          ('Combo-boxes(TBD)', 'combo' ),
          ('Simple Rolodex-like form', 'form' ),

          ('Text', None ),
          ('Basic editable text', 'text' ),
          ('Text display styles', 'style' ),
          ('Hypertext(tag bindings)', 'bind' ),
          ('A text widget with embedded windows and other features(Broken)', 'twind' ),
          ('A search tool build with a text widget', 'search' ),
          ('Peering text widgets(TBD)', 'textpeer' ),
          
          ('Canvases', None ),
          ('The canvas item types(Broken)', 'items' ),
          ('A simple 2-D plot', 'plot' ),
          ('Text items in canvases', 'ctext' ),
          ('An editor for arrowheads on canvas lines', 'arrow'),
          ('A ruler with adjustable table stops', 'ruler' ),
          ('A building floor plan(TBD)', 'floor' ),
          ('A simple scrollable canvas(TBD)', 'cscroll' ),
          ('A Knight\'s tour of the chess board(TBD)', 'knightstour' ),
          
          ('Scales and Progress Bars', None ),
          ('Horizontal scale', 'hscale' ),
          ('Vertical scale', 'vscale'),
          ('Themed scale linked to a label with traces(TBD)', 'ttkscale' ),
          ('Progress bar(TBD)', 'ttkprogress' ),

          ('Paned Windows and Notebooks', None ),
          ('Horizontal paned window(TBD)', 'paned1' ),
          ('Vertical paned window(TBD)', 'paned2' ),
          ('Themed nested panes(TBD)', 'ttkpane' ),
          ('Notebook widget(TBD)', 'ttknote' ),
          
          ('Menus and Toolbars', None ),
          ('Menus and cascades (sub-menus)', 'menu' ),
          ('Menu-buttons(Broken)', 'menubu' ),
          ('Themed menu buttons(TBD)', 'ttkmenu' ),
          ('Themed toolbar(TBD)', 'toolbar' ),
          
          ('Common Dialogs', None ),
          ('Message boxes', 'msgbox' ),
          ('File selection dialog', 'filebox' ),
          ('Color picker(Broken)', 'clrpick' ),
          ('Font selection dialog(TBD)', 'fontchoose' ),
          
          ('Animation', None ),
          ('Animated labels(TBD)', 'anilabel' ),
          ('Animated wave(TBD)', 'aniwave' ),
          ('Pendulum simulation(TBD)', 'pendulum' ),
          ('A celebration of Rube Goldberg(TBD)', 'goldberg' ),
          
          ('Miscellaneous', None ),
          ('The builtin bitmaps', 'bitmap' ),
          ('A dialog box with a local grab', 'dialog1'),
          ('A dialog box with a global grab(TBD)', 'dialog2')
          ]


# The demo main window

class DemoMainWindow(Frame):

    def __init__(self,master, title):
        Frame.__init__(self, master)
        self.master.title(title)

        self._create_menu()
        self._create_textarea()
        self._create_statusbar()
        self._fill_textarea()
        self.text['state']='disabled' # no more text insertion
        self.pack(fill=BOTH, expand=1 )

    def _create_menu(self):        
        self.mbar = Menu(self, type='menubar')
        self.master['menu'] = self.mbar

        # create the 'File' menu
        menu = Menu(self.mbar, tearoff=0)
        self.mbar.add_cascade(label='File', underline=0, menu=menu )       
        menu.add_command(label='About...', underline=0,
                         command=self.about_callback,
                         accelerator='F1')
        menu.add_separator()
        menu.add_command(label='Quit', underline=0,
                         command=self.quit_callback,
                         accelerator='Meta-Q')

    def _create_statusbar(self):
        f = Frame(self)
        f.pack(side=LEFT, fill=X, expand=1 )
        self.l_sbar = Label(f, relief=SUNKEN, padx=10)
        self.l_sbar.pack(side=LEFT, fill=X, expand=1)
        self.l_rbar = Label(f, width=10, relief=SUNKEN, padx=5)
        self.l_rbar.pack(side=RIGHT )
        
    def _create_textarea(self):
        f = Frame(self)
        f.pack(side=TOP,fill=BOTH, expand=1 )
        self.text =  Text(f, relief=SUNKEN, border=2,
                          wrap='word', height=40)
        self.text.pack(side=LEFT, fill=Y, expand=1)

        bar = Scrollbar(f)
        bar.pack(side=LEFT, fill=Y, expand=0)
        self.text['yscrollcommand']=bar.set
        bar['command']=self.text.yview

    def _fill_textarea(self):
    
        #create tags to the text styles
        self.text.tag_configure('title_tag', font='Helvetica 10 bold',
                                justify='left',
                                spacing1=5, spacing3=5)
        
        self.text.tag_configure('section_tag',
                                font='Helvetica 10 bold',
                                spacing1=5, spacing3=2)
        
        self.text.tag_configure('introduction_tag', font='Helvetica 8',
                                lmargin1='10p', lmargin2='10p',rmargin='10p',
                                spacing1=5, spacing3=10)
        self.text.tag_configure('demo_tag',
                                font='Helvetica 8',
                                lmargin1='1c', lmargin2='1c',
                                foreground='blue', underline=1,
                                spacing1=3, spacing3=2) 


        #fill the text area

        self.text.insert(END, "Tk Widget Demonstrations - The tkinter Python version\n\n", 'title_tag' )

        self.text.insert(END,
                         'This application provides an MMI for several '+
                         'short scripts that demonstrate what you can do '+
                         'with Python+Tkinter. Each of the numbered lines '+
                         'below describes a demonstration; you can click on '+
                         'it to invoke the demonstration. Once the '+
                         'demonstration window appears, you can click the '+
                         '"See Code" button to see the Python code that '+
                         'created the demonstration. If you wish, you can '+
                         'edit the code and click the "Rerun Demo" button '+
                         'in the code window to reinvoke the demonstration '+
                         'with the modified code [TBC].\n',
                         "introduction_tag" )

        # insert sections and demo titles
        cnt=0
        idx=0
        for description, file in demos :
            if ( file == None ):
                self.text.insert(END, description+'\n', 'section_tag' )
                idx=0
            else:
                self.text.insert(END, str(idx)+'. '+description+'.\n', ('demo_tag', cnt))
                
                # bind events
                self.text.tag_bind(cnt, '<Any-Enter>',
                                   callit(self.demoenter_callback, cnt) )
                self.text.tag_bind(cnt, '<Any-Leave>',
                                   callit(self.demoleave_callback, cnt) )
                self.text.tag_bind(cnt, '<1>',
                                   callit(self.democlick_callback, cnt) )

            cnt=cnt+1
            idx=idx+1

        
    def about_callback(self):
        pass
        '''
        tk_messageBox -icon info -type ok -title [mc "About Widget Demo"] \
	    -message [mc "Tk widget demonstration application"] -detail \
        "[mc "Copyright \u00a9 %s" {1996-1997 Sun Microsystems, Inc.}]
        [mc "Copyright \u00a9 %s" {1997-2000 Ajuba Solutions, Inc.}]
        [mc "Copyright \u00a9 %s" {2001-2009 Donal K. Fellows}]
        [mc "Copyright \u00a9 %s" {2002-2007 Daniel A. Steffen}]"
        '''


    def demoenter_callback(self, tag):
        #change the color of the entry
        self.text.tag_configure( tag,
                                 foreground='red')
        self.text.configure( cursor='hand2')
        self.l_sbar.configure(text='Run the "' + str(demos[tag][1]) + '" sample program',
                              justify='left')

    def demoleave_callback(self, tag):
        self.text.tag_configure( tag,
                                 foreground='blue' )
        self.l_sbar.configure(text='')
        self.text.configure( cursor='xterm')



    def democlick_callback(self, tag):
        modname = demos[tag][1]
        # import the module and execute the demo
        # this assumes that all modules have a runDemo function
        exec('import %s;%s.runDemo()' % (modname, modname))


    def democlick_callback_2(self, tag):

        file = demos[tag][1]
        #Read the code from the file
        fp = open(file, 'r')
        code=''
        for l in fp.readlines():
            code = code + l
##        run the code
        
        ## for this to work, all demo modules shall be explicitely
        ## imported by this file
#        exec( code )
        rundemo ( code, globals(), locals() )

        
    def quit_callback(self):
        self.destroy()
        sys.exit(0)


if __name__ == "__main__":
    #global TOPLEVEL_TK
    TOPLEVEL_TK = Tk()
    dw = DemoMainWindow(TOPLEVEL_TK, "Tk widget tour - the Python version")
    mainloop()

