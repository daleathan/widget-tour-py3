
The following sub-directories contain pieces of the widget-demo code that
highlighted problems in python-tk (more Tkinter than python)

** segfault contains code that triggers a segmentation fault in the python
   interpreter, version 1.5, 1.6 and 2.0. A bug report has been filed and
   the probem is fixed with 2.1

** hangs_problem contains code that triggers an apparently infinite loop
   (with CPU usage which goes through the roof); the reason is the usage
   of pack and grid functions in the same window.

** image contains code that document a small problem in using images with
   python tk, as well as its workaround.
