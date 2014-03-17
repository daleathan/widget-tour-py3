from tkinter import *

from infrastructure import DemoWindow, callit, demo_path
      
from canvasplot import CanvasPlot


class EmbedTextDemo(DemoWindow):
    """A class demoing a text widget embedding other widgets"""
    def __init__(self):
        DemoWindow.__init__(self, '', demo_path('twind.py') )

        frame = Frame(self); frame.pack(expand=Y, fill=BOTH )
        self.frame=frame
        frame.rowconfigure(0, weight=1 )
        frame.columnconfigure(0, weight=1 )
        self.text=Text(frame, relief=SUNKEN, bd=2, setgrid=1,
                  wrap='word', height=35);
        self.text.grid(row=0,column=0, sticky='nsew')
        bar=Scrollbar(frame); bar.grid(row=0,column=1,sticky='nsew')
        self.text['yscrollcommand']=bar.set; bar['command']=self.text.yview

        self.hscroll = None # preset is needed because it is checked in the
        self.plot = None    # callbacks

        #these are the buttons which will be embedded in the text
        self.b_turnon = Button(self.text, text='Turn On', cursor='top_left_arrow',
                               command = self.turnon_callback )
        self.b_turnoff = Button( self.text, text='Turn Off',
                                 cursor='top_left_arrow',
                                 command=self.turnoff_callback )
        self.b_clickhere = Button(self.text,  text='Click Here',
                                  cursor='top_left_arrow',
                                 command=self.clickhere_callback )
        self.b_delete = Button( self.text,text='Delete',
                                cursor='top_left_arrow',
                                 command=self.delete_callback )

        # insert text and embedding buttons
        self.text.insert(END,
                         "A text widget can contain other widgets embedded "+
                         "in it.  These are called \"embedded windows\", "+
                         "and they can consist of arbitrary widgets.  "+
                         "For example, here are two embedded button "+
                         "widgets.  You can click on the first button to " )
        self.text.window_create(END, window=self.b_turnon )
        self.text.insert(END,
                         " horizontal scrolling, which also turns off "+
                         "word wrapping.  Or, you can click on the second "+
                         "button to " )
        self.text.window_create(END, window=self.b_turnoff )
        self.text.insert(END,
                    "horizontal scrolling and turn back on word wrapping.\n\n" 
                         )
        self.text.insert(END,
                         "Or, here is another example.  If you ")
        self.text.window_create(END, window=self.b_clickhere )
        self.text.insert(END,
                         "a canvas displaying an x-y plot will appear right "+
                         "here." )

        # insert a mark where the plot window shall be inserted
        self.text.mark_set('plot', INSERT )
        self.text.mark_gravity('plot', LEFT)
        
        self.text.insert(END,
                         "\nYou can drag the data points around with "+
                         "the mouse, or you can click here to ")
        self.text.window_create(END, window=self.b_delete )
        self.text.insert(END, " the plot again.\n\n")

        
        self.text.insert(
            END,
            "You may also find it useful to put embedded windows in "
            "a text without any actual text.  In this case the "+
            "text widget acts like a geometry manager.  For "+
            "example, here is a collection of buttons laid out "+
            "neatly into rows by the text widget.  These buttons "+
            "can be used to change the background color of the "+
            "text widget (\"Default\" restores the color to "+
            "its default).  If you click on the button labeled "+
            "\"Short\", it changes to a longer string so that "+
            "you can see how the text widget automatically "+
            "changes the layout.  Click on the button again "+
            "to restore the short string.\n" )

        self.var = StringVar(self.text)
        self.var.set('Short')
        tb = Checkbutton( self.text, indicatoron=0,
                          textvariable=self.var,
                          variable=self.var,
                          offvalue='Short',
                          onvalue='A much longer string',
                          cursor='top_left_arrow',
                          padx=2, pady=4)
        self.text.window_create(END, window=tb )
        
        colors = ( 'AntiqueWhite3', 'Bisque1', 'Bisque2', 'Bisque3', 'Bisque4',
	'SlateBlue3', 'RoyalBlue1', 'SteelBlue2', 'DeepSkyBlue3', 'LightBlue1',
	'DarkSlateGray1', 'Aquamarine2', 'DarkSeaGreen2', 'SeaGreen1',
	'Yellow1', 'IndianRed1', 'IndianRed2', 'Tan1', 'Tan4' )

        c = self.text['background']
        db = Button(self.text, text='Default', background=c,
                    command=callit(self.button_callback, c ),
                    cursor = 'top_left_arrow' )
        self.text.window_create(END, window=db)
                    
        for c in colors:
            b = Button(self.text, text=c, background=c,
                       padx=2, pady=4,
                       cursor='top_left_arrow',
                       command=callit(self.button_callback, c ))
            self.text.window_create(END, window=b)
            
        
    def turnon_callback(self):
        self.hscroll = Scrollbar(self.frame, orient='horizontal',
                                 command=self.text.xview)
        self.hscroll.grid(row=1,column=0,sticky='we')
        self.text['xscrollcommand'] = self.hscroll.set
        self.text['wrap'] = NONE


    def turnoff_callback(self):
        if self.hscroll:
            self.text['xscrollcommand'] = '' 
            self.text['wrap'] = WORD
            self.hscroll.destroy()
            self.hscroll = None
        

    def clickhere_callback(self):
        if not self.plot:
            self.plot = CanvasPlot(self.text)
            self.text.window_create('plot', window=self.plot ) 

    def delete_callback(self):
        if self.plot :
            self.plot.destroy()
            self.plot=None


    def button_callback(self, color):
        self.text['bg'] = color
        

runDemo = EmbedTextDemo


if __name__ == '__main__' :
    demo = EmbedTextDemo()
    mainloop()

