#ifndef _TEXTOBSERVER_H_
#define _TEXTOBSERVER_H_

#include "observer.h"
#include "subject.h"

class TextObserver : public Observer {
public:
  Subject *subject;
  int top, bottom, left, right;
  void notify() override;
  TextObserver(Subject *subject, int top, int bottom, int left, int right);
  ~TextObserver();
};
#endif
