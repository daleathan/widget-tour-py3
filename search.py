# --- text-search.py
# A demonstration of the search capabilities of a text widget
#
from tkinter import *
import tkinter.messagebox as tkMessageBox

from infrastructure import DemoWindow

class SearchDemo(DemoWindow):

    def __init__(self):
        DemoWindow.__init__(self, '', 'search.py' )

        frame = Frame(self); frame.pack(expand=Y, fill=BOTH)
        
        # create the controls panel
        c_frame = Frame(frame); c_frame.pack(side=TOP,expand=Y,fill=X)
        c_frame.columnconfigure(1, weight=1,minsize=300 )

        file_l=Label(c_frame, text='File name:');
        file_l.grid(row=0,column=0, sticky='w')

        self.filevar=StringVar(c_frame)
        self.file_e=Entry(c_frame, textvariable=self.filevar );
        self.file_e.grid(row=0, column=1, sticky='ew')
        self.file_e.bind('<Return>', self.load_callback )

        self.load_b =Button(c_frame, text='Load file', padx=10,
                            command=self.load_callback )
        self.load_b.grid(row=0, column=2, sticky='e' )

        string_l=Label(c_frame, text='Search string:')
        string_l.grid(row=1,column=0)

        self.stringvar=StringVar(c_frame)
        self.string_e=Entry(c_frame, textvariable=self.stringvar );
        self.string_e.grid(row=1, column=1, sticky='ew')
        self.string_e.bind('<Return>', self.hilight_callback )

        self.hilight_b =Button(c_frame, text='Hilight', padx=10,
                               command=self.hilight_callback )
        self.hilight_b.grid(row=1, column=2 )

        # create the text widget and related scrollbar
        t_frame = Frame(frame); t_frame.pack(side=TOP,expand=YES,fill=BOTH)
        self.text = Text(t_frame, wrap='word', setgrid=1 )
        self.text.pack(side=LEFT, expand=YES, fill=BOTH )
        vbar = Scrollbar(t_frame, command=self.text.yview )
        vbar.pack(side=LEFT, fill=Y )
        self.text['yscrollcommand'] = vbar.set

        self.text.insert(END,
                         'This window demonstrates how to use the tagging '+
                         'facilities in text widgets to implement a searching '
                         'mechanism.  First, type a file name in the top '+
                         'entry, then type <Return> or click on "Load File".'+
                         'Then type a string in the lower entry and type '+
                         '<Return> or click on "Hilight".  This will cause '+
                         'all of the instances of the string to be tagged ' +
                         'with the tag "search", and it will arrange for the '+
                         'tag\'s display attributes to change to make all '+
                         'of the strings blink.' )

        self.blink='stop'
        self.timer = None

        # set a callback on window closure to remove timer
        self.wm_protocol('WM_DELETE_WINDOW', self.close )
        

    def load_callback(self, *ignored):
        fname = self.filevar.get()
        if fname:
            try:
                file = open(fname,'r')

                # clear text and stop blinking
                self.text.delete('1.0', END)
                self.blink = 'stop'
                
                line = file.readline()
                while line :
                    self.text.insert(END, line )
                    line = file.readline()
                file.close()
            except IOError:
                ex,arg,traceback = sys.exc_info()
                desc = "%s:%s" % (str(ex),str(arg))
                tkMessageBox.showerror(
                    title='I/O Error',
                    message='Exception:'+'desc') 


    def do_blink (self):
        "Periodically blink on/off text tagged with 'search'"

        if self.blink == 'stop' :
            self.timer = None
            return
        
        if ( self.blink == 'on' ):
            self.blink = 'off'
            if self.winfo_depth() > 1 :
                self.text.tag_configure('search',
                    background='#ce5555', foreground='black' )
            else:
                self.text.tag_configure('search',
                    background='white', foreground='black' )
                
        elif self.blink == 'off':
            self.blink='on'
            self.text.tag_configure('search',
                                   background='', foreground='' )

        # schedule next blink
        self.timer = self.after( 1000, self.do_blink )


    def hilight_callback(self, *ignored):

        string = self.stringvar.get()

        # remove old tags
        self.text.tag_remove('search', '1.0', END )

        if string :
            len = IntVar(self.text)
            cur = self.text.search(string, '1.0', END, count=len )
            while cur  :
                tag_start = cur 
                tag_end ='%s+%d char'%(tag_start, len.get())
                self.text.tag_add('search', tag_start, tag_end )

                cur = self.text.search(string, tag_end, END, count=len )


            # switch on blinking of tagged text
            self.blink = 'on'
            self.do_blink()

        else:
            # remove blinking
            self.blink = 'stop'
                
                    
    def close(self):
        "It deletes the thimer before destroying the wndow"
        if self.timer:
            self.after_cancel(self.timer)
        self.destroy()


runDemo = SearchDemo

if __name__ == '__main__':
    demo = SearchDemo()
    mainloop()
        

        
        

