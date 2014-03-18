
from tkinter import *
from tkinter.ttk import *

from infrastructure import DemoWindow

class TextTag:
    "A simple class to facilitate the creation of text tags."
    number=0
    def __init__(self, text_widget, **config ):
        self.id = TextTag.number
        TextTag.number = TextTag.number+1
        text_widget.tag_configure( self.id, config )

        

class TaggedTextDemo(DemoWindow):

    def __init__(self):
        DemoWindow.__init__(self, '', 'style.py' )

        frame = Frame(self); frame.pack(expand=Y, fill=BOTH )
        text=Text(frame, relief=SUNKEN, bd=2, setgrid=1, height=35,
                  wrap='word');
        text.pack(side=LEFT, expand=Y, fill=BOTH)
        bar=Scrollbar(frame); bar.pack(side=LEFT, fill=Y)
        text['yscrollcommand']=bar.set; bar['command']=text.yview

        # create the tags
        bold = TextTag(text,font='Courier 12 bold italic')
        big = TextTag(text, font='Courier 14 bold')
        verybig = TextTag(text, font='Helvetica 24 bold')

        if self.winfo_depth() > 1 :
            color1 = TextTag(text, background='#a0b7ce')
            color2 = TextTag(text, foreground='red')
            raised = TextTag(text, relief='raised', borderwidth=1 )
            sunken = TextTag(text, relief='sunken', borderwidth=1 )
        else:
            color1 = TextTag(text, background='black', foreground='2hite')
            color2 = TextTag(text, background='black', foreground='white')
            raised = TextTag(text, background='white', relief='raised',
                             borderwidth=1 )
            sunken = TextTag(text, background='white', relief='sunken',
                             borderwidth=1 )

        bgstipple = TextTag(text, background='black', borderwidth=0,
                            bgstipple='gray12' )
        fgstipple = TextTag(text, fgstipple='gray50')
        underline = TextTag(text, underline='on')
        overstrike = TextTag(text, overstrike='on')
        right=TextTag(text, justify='right')
        center=TextTag(text, justify='center')
        super = TextTag(text, offset='4p', font='Courier 10')
        sub = TextTag(text, offset='-2p', font='Courier 10')
        margins = TextTag(text, lmargin1='12m', lmargin2='6m',
                          rmargin='10m' )
        spacing = TextTag(text, spacing1='10p', spacing2='2p',
                          lmargin1='12m', lmargin2='6m', rmargin='10m')

        # insert tagged text

        tagged_text = (
            ( 'Text widgets like this one allow you to display information'+
              ' in a variety of styles.  Display styles are controlled using' +
              ' a mechanism called ',
              None ),
            ( 'tags', bold.id ),
            ( '\n Tags are just textual names that you can apply to one '+
              'or more ranges of characters within a text widget.  You can '+
              'configure tags with various display styles.  If you do this,'+
              ' then the tagged characters will be displayed with the styles '+
              'you chose. \nThe available display styles are:',
              None ),
            ( '\n1. Font.', big.id ),
            ( '  You can choose any X font, ', None ),
            ( 'large', verybig.id ),
            ( ' or ', None ),
            ( 'small.\n', None ),
            ( '\n2. Color.', big.id ),
            ( '  You can change either the ', None ),
            ( 'background', color1.id ),
            ( ' or ', None ),
            ( 'foreground', color2.id ),
            ( ' or ', None ),
            ( 'both.\n', (color1.id, color2.id ) ),
            ( '\n3. Stippling.', big.id ),
            ( '  You can cause either the ', None ),
            ( 'background ', bgstipple.id ),
            ( ' or ', None ),
            ( 'foreground', fgstipple.id ),
            ( ' information to be drawn with a stipple instead of a solid fill. \n', None ),
            ( '\n4. Underlining.', big.id ),
            ( '  You can ', None ),
            ( 'underline', underline.id ),
            ( ' ranges of text. \n', None ),
            ( '\n5.  Overstrikes.', big.id ),
            ( '  You can ', None ),
            ( 'draw lines through', overstrike.id ),
            ( ' ranges of text.\n', None ),
            ( '\n6. 3-D effects.', big.id ),
            ( '  You can arrange for the background to be drawn with a '+
              'border that makes characters appear either ', None ),
            ( 'raised', raised.id ),
            ( ' or ', None ),
            ( 'sunken', sunken.id ),
            ( '\n', None ),
            ( '\n7. Justification.', big.id ),
            ( '  You can arrange for lines to be displayed\n', None ),
            ( 'left-justified,\n', None ),
            ( 'right-justified, or\n', right.id ),
            ( 'centerer.\n', center.id ),
            ( '\n8. Superscripts and subscripts.', big.id ),
            ( '  You can control the vertical position to generate '+
              'superscript effects like 10', None ),
            ( 'n', super.id ),
            ( ' or subscript effects like X', None ),
            ( 'i', sub.id ),
            ( '.\n', None ),
            ( '\n9. Margins.', big.id ),
            ( '  You can control the amount of extra space left on '+
              'each side of the text:\n', None ),
            ( 'This paragraph is an example of the use of '+
              'margins. It consists of a single line of text '+
              'that wraps around the screen. There are two '+
              'separate left margins values, one for the first '+
              'display line associated with the text line, ' +
              'and one for the subsequent display lines, which '+
              'occur because of wrapping. There is also a '+
              'separate specification for the right margin, which '+
              'is used to choose wrap points for lines. \n',
              margins.id ),
            ( '\n10. Spacing.', big.id ),
            ( 'You can control the spacing of lines with three '+
              'separate parameters. "Spacing1" tells how much '+
              'extra space to leave above a line, '+
              '"spacing 3" tells how much space to leave below a line'+
              ' and if a line wraps, "spacing2" tells how much space to leave'+
              ' between the display lines that make up the text line.\n',
              None ),
            ( 'These indented paragraphs illustrates how spacing '+
              'can be used. Each pharagraph is actually a '+
              'single line in the text widget, which is '+
              'word-wrapped by the widget.\n', spacing.id ),
            ( 'Spacing1 is set to 10 points for this text, '+
              'which results in relatively large gaps between '+
              'the paragraphs. Spacing2 is set to 2 points, '+
              'which results in just a bit of extra space within a '+
              'paragraph. Spacing3 isn\'t used in this example.',
              spacing.id ),
            ( '\nTo see where the space is, select ranges of text '+
              'within these paragraphs. The selection hilight will cover'+
              ' the extra space.', spacing.id )
        )
        

        for txt, tags in tagged_text: 
            text.insert(END, txt, tags )

        
runDemo = TaggedTextDemo

if __name__ == '__main__':
    demo = TaggedTextDemo()
    mainloop()

