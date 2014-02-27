
import sys, subprocess

from tkinter import *

from infrastructure import DemoWindow, callit
      
def filexec(fname):
    # FIXME : there should be a way to derive the path of interpreter
    try:
        subprocess.Popen( "python3 "+fname, shell=True)
    except:
        print( "Cannot execute %s : %s" % ( fname, sys.exc_info()[1] ) ) 

class HyperTextDemo(DemoWindow):

    def __init__(self):
        DemoWindow.__init__(self, '', 'hypertext.py' )

        frame = Frame(self); frame.pack(expand=Y, fill=BOTH )
        text=Text(frame, relief=SUNKEN, bd=2, setgrid=1,
                  wrap='word', height=35);
        text.pack(side=LEFT, expand=Y, fill=BOTH)
        bar=Scrollbar(frame); bar.pack(side=LEFT, fill=Y)
        text['yscrollcommand']=bar.set; bar['command']=text.yview

        self.text = text
        
        self.tags = range(0,6)
        # create and binds the tags
        for t in self.tags:
            self.text.tag_configure (t)
            self.text.tag_bind(t, '<Any-Enter>',
                               callit(self.reconfigure_tag, t, 'bold' ))
            self.text.tag_bind(t, '<Any-Leave>',
                               callit(self.reconfigure_tag, t, 'normal' ))
            self.text.tag_bind(t, '<1>',
                               callit(self.link_callback, t ))
                 
                               
            
        # insert tagged text
        intro = """
The same tag mechanism that controls display styles in text widgets can also be used to associate Tcl commands with regions of text, so that mouse or keyboard actions on the text cause particular Tcl commands to be invoked.  For example, in the text below the descriptions of the canvas demonstrations have been tagged.  When you move the mouse over a demo description the description lights up, and when you press button 1 over a description then that particular demonstration is invoked.


"""
        text.insert('0.0', intro )
        text.insert( END,
                     '1. Samples of all the different types of items that'+
                     ' can be created in canvas widgets.',
                     self.tags[0] )
        text.insert( END, '\n\n');
        text.insert( END,
                     '2. A simple two-dimensional plot that allows you '+
                     'to adjust the positions of the data points.',
                     self.tags[1] )
        text.insert( END, '\n\n');
        text.insert( END,
                     '3. Anchoring and justification modes for text items.',
                     self.tags[2] )
        text.insert( END, '\n\n');
        text.insert( END,
                     '4. An editor for arrow-head shapes for line items.',
                     self.tags[3] )
        text.insert( END, '\n\n');
        text.insert( END,
                     '5. A ruler with facilities for editing tab stops.',
                     self.tags[4] )
        text.insert( END, '\n\n');
        text.insert( END,
                     '6. A grid that demonstrates how canvases can be '+
                     'scrolled.',
                     self.tags[5] )


    
    def reconfigure_tag(self, which, how ):
        if self.winfo_depth() > 1 :
            if ( how == 'bold' ):
                self.text.tag_configure( which,
                                         background='#43ce80',
                                         relief='raised',
                                         borderwidth=1 )
            elif ( how == 'normal' ):
                self.text.tag_configure(which,
                                        background='', relief='flat' )
        else:
            if ( how == 'bold' ):
                self.text.tag_configure(which,
                                        foreground='white',
                                        background='black' )
            elif ( how == 'normal' ):
                self.text.tag_configure( foreground='',
                                         background='' )


    def link_callback(self, which ):
        files = ( 'canvasitems.py',
                  'canvasplot.py',
                  'canvastext.py',
                  'arrowhead.py',
                  'canvasruler.py',
                  'canvasscroll.py' )
        filexec(files[which])



runDemo = HyperTextDemo

if __name__ == '__main__':
    demo = HyperTextDemo()
    mainloop()
