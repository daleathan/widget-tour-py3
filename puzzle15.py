
from tkinter import *
import random

import infrastructure

class PuzzleButton(Button):
    "A button with additional info"

    def __init__(self, master, v, r, c ):
        self.board_width, self.board_height= (
            int(master['width']), int(master['height']) )
        self.dx = self.board_width/4
        self.dy = self.board_height/4

        Button.__init__(self, master, text='%2d'%(v) )
        

##        self.grid(row=r, column=c,sticky='nsew')
        self.place(x=int(self.dx*r),
                   y=int(self.dy*c),
                   width=int(self.dx),
                   height=int(self.dy) )
                        
        self.row = r
        self.column=c
        self.value=v


    def move(self, r, c):
#        self.grid(row=r,column=c, sticky='nsew')
        self.place(x=int(self.dx*r),
                   y=int(self.dy*c),
                   width=int(self.dx),
                   height=int(self.dy))
        self.row=r
        self.column=c
        


class Puzzle15( infrastructure.DemoWindow ):
    """
    A class to play the 15-puzzle games
    There are a few changes wrt the tcl/tk version of this demo:
    - pseudo-random scrambling of the puzzle
    - used a matrix of buttons instead of reasoning directly on
      buttons coordinates
    """

    def __init__(self):
        l ="""A 15-puzzle appears below as a collection of buttons.
        Click on any of the pieces next to the space, and that piece
        will slide over the space.  Continue this until the pieces are
        arranged in numerical order from upper-left to lower-right."""

        infrastructure.DemoWindow.__init__(self, l, 'puzzle15.py' )

        # create the buttons container
        frame = Frame(self, relief=SUNKEN, border=2,
                      background='darkgray',
                      width=100, height=100)
        frame.pack( pady=10,expand=NO, fill=NONE)

        # define the initial position
        start_sequence = [x for x in range(1,16)]+[0,]

        # create and place buttons
        self.buttons = [] # this will be a matrix
        cnt=0
        for v in start_sequence:
            r, c = cnt//4, cnt%4 
                            
            if cnt % 4 == 0 :
                self.buttons.append([]) # create a new row
            if v : # zero means empty place
                b = PuzzleButton(frame, v, r, c )
                b['command'] = infrastructure.callit(self.callback, b)
                self.buttons[r].append(b)
            else:
                self.buttons[r].append(None)
                
            cnt=cnt+1

        # make a number of arbitrary moves to scramble the puzzle
        for i in range(1,1000):
            row = random.choice(self.buttons)
            b = random.choice(row)
            if b:
                self.callback(b)
                

    def callback( self, button ):
        r,c = button.row, button.column
                
        empty = None
        if r>0 and not self.buttons[r-1][c]: #up place is empty
            empty = (r-1, c)
            
        if c>0 and not self.buttons[r][c-1]: #left place is empty
            empty = (r, c-1)

        if r<3 and not self.buttons[r+1][c]: #down place is empty
            empty = (r+1,c)
            
        if c<3 and not self.buttons[r][c+1]: #up place is empty
            empty = (r, c+1)

        if empty:
            r1,c1 = empty

            self.buttons[r][c].move(r1,c1)
            self.buttons[r][c], self.buttons[r1][c1] = (
                self.buttons[r1][c1], self.buttons[r][c] )

        
def runDemo():
    Puzzle15()

        
if __name__ == '__main__' :
    demo = Puzzle15()
    mainloop()
            



