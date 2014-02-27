# infrastructure.py --
#
# This module contains the common infra-structures needed by all the demo
# programs of widget-demo, which aims to duplicate in pyton/Tkinter the
# functionalitis of the useful widget demo shipped with the Tcl/Tk tools
#

from Tkinter import *
from string import *



class SeeCodeWindow( Toplevel ):
    """
    This is the window which shows the code related to a demo
    It is composed of the following elements :
    -   A scrollable text widget, containing the thext of the file;
        It also allows to edit the code
    -   A dismiss button, which closes the window
    -   A run demo, wich rerurn the demo with the edited code in the
        window
    This class shall be create in a single instance.
    """

    instance = None

    def __init__(self):

        Toplevel.__init__( self )

        SeeCodeWindow.instance = self

        # This is the frame which holds toghether text widget
        # and scrollbars
        text_frame = Frame(self)
        text_frame.pack( side=TOP, expand=YES, fill=BOTH )

        # Create a text widget and a scrolled bar and bind them
        # toghether
        scrollbar = Scrollbar( text_frame )
        scrollbar.pack( fill=Y, side=RIGHT )
        # the text widget is referred in other methods,
        # so I'll use an attribute to store it
        self.text = Text( text_frame,
                          wrap=WORD, width=60, height= 30,
                          padx=4, pady=2, takefocus=0,
                          yscrollcommand=scrollbar.set )
        self.text.pack( side=RIGHT, expand=YES, fill=BOTH )
        
        # I like the fact that config options are mapped this way
        scrollbar['command'] = self.text.yview

        # add the two buttons, in a second frame
        button_frame = Frame( self )
        button_frame.pack( side=TOP, expand=YES, fill=X )

        b_dismiss=Button( button_frame, text='Dismiss',
                          command=self.dismiss_callback )
        b_restart=Button( button_frame, text='Rerun Demo',
                          command=self.rerun_callback )
        
        for b in b_dismiss, b_restart : b.pack( side=LEFT, padx=3, pady=2,
                                                expand=YES, fill=BOTH )
    

    def showcode( self, filename ):

        fp = open( filename, 'r' )

        #lets try to slurp all the file in a stroke, it should not be so long
        for l in fp.readlines():
            self.text.insert(END, l )


    def dismiss_callback(self):
        SeeCodeWindow.instance = None
        self.destroy()


    def rerun_callback(self):
        # 1.0 here means line 1(first), character 0
        new_code=  self.text.get('1.0', END )

        # run the code, possibly modified
        new_locals, new_globals = locals(), globals()
        exec (new_code, new_locals, new_globals)
        rundemo(str(self.__class__), new_locals, new_globals)
        

# ============================================================================
        
def ShowCode( filename ):
    """
    A little convenience function to check and create
    the unique instance of the SeecodeWindow, before using it
    """
    if ( SeeCodeWindow.instance == None ):
        SeeCodeWindow()

    SeeCodeWindow.instance.showcode( filename )
    

    
# ============================================================================
class DemoWindow( Toplevel ):
    """
    I noted that most of the windows demostrating demos have the
    same structure :
    - One label at the top which explains the demo
    - A central area, wich contains the objects topics of the demo
    - Two buttons on the bottom :
         - A dismiss button, which closes the window
         - A See code show code button, which shows a window with the code
    There is enough commonalities to justify a common super-class, from
    which all the demo windows are derived
    """
    instance = None
    
    def __init__( self,  introduction, code_file ):
        Toplevel.__init__(self)
        
        DemoWindow.instance = self

        # store object attributes
        self.code_file = code_file

        # create and pack the introduction label
        intro_label=Label(self, text=introduction)
        intro_label.pack(side=TOP)

        # this is the frame which contains the two buttons at the end
        button_frame = Frame( self )
        button_frame.pack( side=BOTTOM, pady='2m', fill=X )
        
        #create the two buttons and pack them
        dismiss_button = Button(  button_frame, text='Dismiss',
                                  command=self.dismiss_callback )
        seecode_button = Button( button_frame, text='See code',
                                 command=self.seecode_callback )

        # the loop is not needed, for two elements, but I wanted to emulate
        # the powerful Tk pack command, which can pack many widgets at once
        for b in (dismiss_button, seecode_button) :
            b.pack( side=LEFT, expand=YES, padx=10, pady=10, fill=BOTH )

    #
    # The callbacks activated by the two buttons
    #
    def dismiss_callback(self):
        self.destroy()

    def seecode_callback(self):
        ShowCode( self.code_file )


# ============================================================================
class callit:
    """
    This little class helps me to call a callback with command option
    passing parameters to it
    The trick is in the definition of __call__, so that an instance of
    this class can replace a function
    """
    def __init__(self, function, *args ):
        self.f = function
        self.args = args

    def __call__(self, *ignored):
        apply(self.f, self.args)
        

# ============================================================================

_CurrentDemo = None

def rundemo(demo_class, local_dict=locals(), global_dict=globals()):
    """
    It starts a new demo
    """
    if _CurrentDemo :
        _CurrentDemo.destroy()

    cmd = '_CurrentDemo=%s()' % demo_class
    print cmd

    exec (cmd, local_dict, global_dict)

    


def stopdemo():
    """
    Called by the demo master to stop the demo
    """
    if _CurrentDemo : _CurrentDemo.delete()
    _CurrentDemo = None
    
    



# ---------------------------------------------------------------------------
# module self-test code

class MyDemoWindow(DemoWindow):
    def __init__(self):
        l = """This is the self test of
        infrastructure module"""
        DemoWindow.__init__(self,l, 'infrastructure.py')




if __name__ == '__main__' : 

    def selftest():
        """
        The self-test of this module
        """
            
        rundemo('MyDemoWindow', locals(), globals())
    
        mainloop()                 
    
    selftest()





