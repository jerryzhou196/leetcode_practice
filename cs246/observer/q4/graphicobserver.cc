#include "graphicobserver.h"
#include <string>

GraphicObserver::GraphicObserver(Subject *subject, int top, int bottom,
                                 int left, int right)
    : subject{subject}, top{top}, bottom{bottom}, left{left}, right{right} {
  window = new Xwindow(10 * (right - left + 1), 10 * (bottom - top + 1));
  subject->attach(this);
}

GraphicObserver::~GraphicObserver() { subject->detach(this); }

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

void GraphicObserver::notify() {
  // window->fillRectangle(10, 10, 10, 10, Blue);
  window->drawString(10, 20, "High Score:");
  window->drawString(10, 50, "Score:");

  // for (int y = top; y < bottom + 1; ++y) {
  //   for (int x = left; x < right + 1; ++x) {
  //     const char c = subject->getState(y, x);

  //     if (isdigit(c)) {
  //       window->fillRectangle((x - left) * 10, (y - top) * 10, 10, 10, Blue);
  //     } else if (isupper(c)) {
  //       window->fillRectangle((x - left) * 10, (y - top) * 10, 10, 10,
  //       Green);
  //     } else if (islower(c)) {
  //       window->fillRectangle((x - left) * 10, (y - top) * 10, 10, 10, Red);
  //     } else if (c == ' ') {
  //       window->fillRectangle((x - left) * 10, (y - top) * 10, 10, 10,
  //       White);
  //     } else {
  //       window->fillRectangle((x - left) * 10, (y - top) * 10, 10, 10,
  //       Black);
  //     }
  //   }
  // }
}
