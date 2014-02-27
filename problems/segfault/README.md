
The program in this archive make the C Python interpreter to
crash, apparently in the _tkinter module.

The bug can be verified simply by running 'python buttons.py'.
The bug is triggered by a syntax error in the file buttons.py.
The error is marked by a comment (search for BUG!). Removing
the syntax error, the crash does not happen anymore. 

The bug has been verified on the following platforms:

Python 1.53 + Solaris 7 
Python 1.53 + Linux GNU/Debian 
Python 1.6  + Linux GNU/Debian 2.2

On Solaris, the debugger(gdb) extracted this info from the core file:

AsString (value=0x0, tmp=0x1f4400) at ./_tkinter.c:320
        320                     Py_DECREF(v);


UPDATE: A bug was reported and fixed as for Python 2.1



