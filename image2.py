
from tkinter import *
from tkinter.ttk import *

from tkinter.messagebox import showerror
import glob

from infrastructure import DemoWindow, demo_path
from common import HScrollList

class ImageIFDemo( DemoWindow ):

    def __init__(self):
        l = """This demonstration allows you to view images using a Tk "photo"
        image.  First type a directory name in the text entry, then type Return
        to load the directory into the listbox.
        Then double-click on a file name in the listbox to see that image.
        """
        DemoWindow.__init__(self,l,demo_path('image2.py'))

        frame=Frame(self);frame.pack(side=TOP,expand=YES,fill=BOTH)
        self.frame = frame
        
        #create the directory entry
        label_dir = Label(frame, text='Directory:')
        label_dir.pack(side=TOP, pady=5)
        self.entry_dir = Entry(frame)
        self.entry_dir.pack(side=TOP,expand=YES, fill=X )

        # define the callback to call when user enters <return> in the entry
        self.entry_dir.bind('<Return>', self.entry_callback )
            
        # create and pack the list of image files
        label_file = Label(frame, text='File:')
        label_file.pack(side=TOP, pady=10 )
        self.list_file = HScrollList(frame)
        self.list_file.pack(side=TOP, expand=YES, fill=X)

        self.list_file.list.bind('<Double-1>', self.list_callback )
        
        #create the label which contains the image and its title
        self.image_title = Label(frame, text='Image:')
        self.image_title.pack(side=TOP, pady=10 )
        self.image_label = Label(frame)
        self.image_label.pack(side=TOP )

        #pre-set interface to image subdirectory
        self.entry_dir.insert(0,'images')
        self.entry_callback()


    def entry_callback(self, *ignored):
        dir = self.entry_dir.get()
        self.list_file.list.delete(0,END)
        for file in glob.glob(dir+'/*.*'):
            self.list_file.list.insert(END, file)

    def list_callback(self, event):

        filename = self.list_file.list.get(
            self.list_file.list.nearest(event.y))

#        print 'selected:'+ `filename`
            
        try:
            self.image = PhotoImage(master=self, file=filename)
            self.image_title['text']= 'Image :'+filename
            self.image_label['image'] = self.image
            
        except TclError:
            showerror(
                message=('%s is not a valid image file' % filename)
                )

runDemo = ImageIFDemo

if __name__ == '__main__':
    demo = ImageIFDemo()
    mainloop()

