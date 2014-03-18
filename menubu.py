# ---
# menubu.py : demo of various kind of menu-buttons
#

from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow,demo_path


class MenuButtonsDemo(DemoWindow):

    def __init__(self):
        l = """This is a demonstration of menubuttons. The \"Below\"
        menubutton pops its menu below the button; the \"Right\"
        button pops to the right, etc. There are two option menus
        directly below this text; one is just a standard menu and
        the other is a 16-color palette.
        """
        DemoWindow.__init__(self,l,demo_path('menubu.py'))

        frame= Frame(self);frame.pack( expand=YES, fill=BOTH )
        frame.rowconfigure(1,weight=1, pad=120)
        frame.columnconfigure(1,weight=1,pad=120)

        #create the 'number' option menu in the middle
        middleframe = Frame(frame);middleframe.grid(row=1,column=1)
        var_numbers=StringVar(middleframe);var_numbers.set('One')
        om_numbers= OptionMenu(middleframe,var_numbers,
                               'One', 'Two', 'Three')
        om_numbers.pack(side=LEFT, padx=10)

        #create the 'color' optionmenu in the middle
        colors = ('Black', 'red4', 'DarkGreen', 'NavyBlue',
                  'gray75', 'Red', 'Green', 'Blue', 'gray50',
                  'Yellow', 'Cyan', 'Magenta', 'White',
                  'Brown', 'DarkSeaGreen', 'DarkViolet' )
        var_colors=StringVar(middleframe);var_colors.set(colors[0])
        var_colors.trace_variable('w', self.colorsupdate_callback )
        om_colors=apply( OptionMenu, (middleframe,var_colors)+colors )
        om_colors['menu'].entryconfigure(len(colors)/3, columnbreak=1)
        om_colors['menu'].entryconfigure(2*len(colors)/3+1, columnbreak=1)      
        om_colors.pack(side=RIGHT,padx=10)
        print(om_colors)
        print(om_colors['menu'])
        # set images for color menu options
        self.images=[]
        for i in range(0,len(colors)):
            img = PhotoImage(name='image_'+colors[i],
                             height=16,width=16)
            self.images.append(img) # images shall live as long as the menu
            img.put(colors[i], to=(0,0,15,15))
            om_colors['menu'].entryconfigure(i, image=img )

        # for some reason, if this is done before the above loop,
        # the menu entries lose the 'image' property
        # Also the tk demo does this at the end
        om_colors['menu'].configure(tearoff=1)        

        # store vars needed for callbacks
        self.var_colors=var_colors
        self.om_colors=om_colors 
        
        #create the four menu buttons at the edge of the frame
        for text,direction,row,column,sticky in (
            ('Above','above',2,1,'s'),
            ('Below','below',0,1,'n'),
            ('Left','left',1,0,'w'),
            ('Right','right',1,2,'e')):
            mb=Menubutton(frame, text=text, underline=0,
                          relief=RAISED, direction=direction )
            menu = Menu(mb, tearoff=0)
            mb['menu']= menu
            menu.add_command(label=text+' menu first option',
                             underline=len(text)+1)
            menu.add_command(label=text+ ' menu second option',
                             underline=len(text)+1)
            mb.grid(row=row,column=column,sticky=sticky)


    def colorsupdate_callback( self, *dontcare ):
        self.om_colors['background']=self.var_colors.get()


runDemo = MenuButtonsDemo

## ----------------------------------------------------------------------------

if __name__ == '__main__':
    demo = MenuButtonsDemo()
    mainloop()

