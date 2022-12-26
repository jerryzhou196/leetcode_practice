#ifndef _GRAPHICOBSERVER_H_
#define _GRAPHICOBSERVER_H_

#include "observer.h"
#include "subject.h"
#include "window.h"

class GraphicObserver : public Observer {
public:
  Subject *subject;
  GraphicObserver(Subject *subject, int top, int bottom, int left, int right);
  int top, bottom, left, right;
  Xwindow *window;
  void notify() override;
  ~GraphicObserver();
};

#endif
