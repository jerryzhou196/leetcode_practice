The code in this directory will not build a complete program.  You will need to
use your solution for Q2 as a starting point.

This directory includes:

* an updated main.cc, with a test harness that recognizes the command set
  for this problem
* the files window.h and window.cc for creating XWindows graphics
* the files subject.h and observer.h, which define the public interface
  for subjects and observers; you will need to supply a subject.cc file
  that completes the implementation of subject.h

You will need to modify the studio class, such that it becomes a subclass
of subject, and such that its printing responsibilities are now delegated
to observer objects.  **Your updated studio class should not print anything.**
This means the functioning of Studio::render will change.

Also remember to add the -X11 linking flag to the linking portion of your
Makefile.
