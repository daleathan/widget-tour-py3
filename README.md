<!-- encoding: UTF-8  -->

# A tour of Tkinter widgets

Duplication of the standard demo suite that comes with Tcl/Tk distribution.

Quick start:

	$ python widget.py

## FEATURES

## DOCUMENTATION

### Wiki

Visit the wiki to see screenshots of each of the examples.

https://github.com/daleathan/widget-tour-py3/wiki

### Requirements

#### Mandatory requirements:

* Python v3.2 or later

* the `tkinter` package must also be installed;

to test if tkinter is installed on your system, from the console terminal:

    $ python

    >>> import tkinter

if you get an error message, `tkinter` is *NOT* installed;

## LICENSE

These files are distributed under the licence "please help yourself" :-)

## Tk Demo
http://core.tcl.tk/tk/tree?ci=tip&name=library/demos

## History

### [ENGLISH]
Hello,

I wrote these demo programs in the summer of 2000, when I needed some practice with python+Tkinter for later work. Rather than inventing new demos, I choose to duplicate the standard demo suite that comes with Tcl/Tk distribution. I got 80% of the job done before the summer vacation run out: enogh for my purpose, so I never completed them. 

More recently, I decided to port these scipts to python3, to get a direct feeling of how much effort such a porting takes. I made it in an afternoon: very few print, but mant backticks (I was fond of them back in 2000), several apply (it was before * and ** function arguments) and also some changes in Tkinter (now tkinter ) modules due to the standardized name convention in python standard library.  

The main module of this program is widget.py. It will display a main window to select and run the various demo. Each demo is a single module.  The modules 'infrastructure' and 'common' contain general-purpuse functions. 

These files are distributed under the licence "please help yourself" :-)

Created by

Francesco Bochicchio

https://mail.python.org/pipermail/tkinter-discuss/2009-July/001999.html

https://mail.python.org/pipermail/tkinter-discuss/2009-August/002044.html

http://tkinter.unpy.net/wiki/A_tour_of_Tkinter_widgets


### [ITALIANO]
Ciao.  

Ho scritto queste demo nell'ormai lontano 2000, quando avevo necessità di fare un  po di pratica con Python+Tkinter. Invece che inventarne di nuove, ho riprodotto un 80% della demo che è distribuita con Tcl/Tk. Alcune demo 
sono ancora da scrivere, altre da completare. 

Più di recente ho porato queste demo in Python3, per avere un feeling di cosa comporta fare una operazione del genere. Per la cronaca, senza usare tool automatici, c'e' voluto un pomeriggio:poche print ma molti apici invertiti (ricordo che mi piacevano parecchio nel 2000), qualche apply per ovviare al fatto che non c'erano ancora i parametri * e ** per le funzioni, e anche qualch cambio di nomi in Tkinter (ora tkinter) per via della standardizzazione della name convention nei moduli della standard library.

Il modulo principale di questo programma e' widget.py. Atrraverso questo modulo potrai lanciare i vari programmi dimostrativi. Ogni demo e' un modulo a se. I moduli 'infrastructure' e 'common' contengono funzioni e classi
utilizzati da tutti i demo.

Questi file sono distribuiti sotto la licenza "serviti pure" :-)
