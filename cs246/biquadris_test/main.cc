#include "window.h"
#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unistd.h>

using namespace std;

int main(void) {

  unsigned long colours[10];

  Display *d = XOpenDisplay(NULL);
  if (d == NULL) {
    cerr << "Cannot open display" << endl;
    exit(1);
  }
  int s = DefaultScreen(d);
  Window w = XCreateSimpleWindow(d, RootWindow(d, s), 10, 10, 1000, 1000, 1,
                                 BlackPixel(d, s), WhitePixel(d, s));
  XSelectInput(d, w, ExposureMask | KeyPressMask);
  XMapRaised(d, w);

  Pixmap pix =
      XCreatePixmap(d, w, 1000, 1000, DefaultDepth(d, DefaultScreen(d)));
  GC gc = XCreateGC(d, pix, 0, (XGCValues *)0);

  XFlush(d);
  XFlush(d);

  // Set up colours.
  XColor xcolour;
  Colormap cmap;
  char color_vals[11][11] = {"white",  "black", "red",    "green",
                             "blue",   "cyan",  "yellow", "magenta",
                             "orange", "brown", "gray"};

  enum {
    White = 0,
    Black,
    Red,
    Green,
    Blue,
    Cyan,
    Yellow,
    Magenta,
    Orange,
    Brown
  };

  cmap = DefaultColormap(d, DefaultScreen(d));
  for (int i = 0; i < 5; ++i) {
    XParseColor(d, cmap, color_vals[i], &xcolour);
    XAllocColor(d, cmap, &xcolour);
    colours[i] = xcolour.pixel;
  }

  XSetForeground(d, gc, colours[Black]);

  // Make window non-resizeable.
  XSizeHints hints;
  hints.flags = (USPosition | PSize | PMinSize | PMaxSize);
  hints.height = hints.base_height = hints.min_height = hints.max_height = 1000;
  hints.width = hints.base_width = hints.min_width = hints.max_width = 1000;
  XSetNormalHints(d, w, &hints);

  XSynchronize(d, True);

  usleep(1000);

  // Make sure we don't race against the Window being shown
  XEvent ev;
  while (1) {
    XNextEvent(d, &ev);
    if (ev.type == Expose)
      break;
  }

  string hs = "High Score";
  XDrawString(d, w, DefaultGC(d, s), 10, 20, hs.c_str(), hs.length());

  string hs_v = "69";
  XDrawString(d, w, DefaultGC(d, s), 100, 20, hs_v.c_str(), hs_v.length());

  string score = "Score";
  XDrawString(d, w, DefaultGC(d, s), 10, 40, score.c_str(), score.length());

  string s_v = "420";
  XDrawString(d, w, DefaultGC(d, s), 100, 40, s_v.c_str(), s_v.length());

  // BOARD LOCATION WILL BE:
  // TOP: y, LEFT: x, BOTTOM: y + (5 * 18), RIGHT: x + (5 * 11)
  // SO WINDOW SIZE MUST BE CORRECT

  // std::vector<std::vector<Block *>> &grid = subject->getGrid();

  // int columns = grid.size();

  // int cur_score = subject->getScore();
  // int high_score = subject->getHighScore(); // NOT IMPLEMENTED BY THEO YET

  // int rows = (columns > 0) ? grid[0].size() : 0;

  // assert(columns == 11);
  // assert(rows == 18);
  XSetForeground(d, gc, colours[colour]);
  XFillRectangle(d, w, gc, 10, 60, 180, 110);
  // for (int row = 0; row < 9; ++row) {
  //   for (int column = 0; column < 15; ++column) {
  //     XFlush(d);

  //     XFlush(d);
  //     // if (row > 3 && row < 12 && column > 3 && columns < 9) {
  //     //   window->fillRectangle(column + 50, row + 10, 5, 5, Gray);
  //     // } else if (grid[row][column]) {
  //     //   window->fillRectangle(
  //     //       column + 50, row + 10, 5, 5,
  //     //       getColor(grid[row][column]->getName())); // MOLLY'S CHAR
  //     // }
  //   }
  // }
  XSetForeground(d, gc, colours[2]);
  return 0;
}
