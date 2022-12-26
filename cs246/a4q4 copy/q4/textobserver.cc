#include "textobserver.h"

#include <iostream>

TextObserver::TextObserver(Subject *subject, int top, int bottom, int left,
                           int right)
    : subject{subject}, top{top}, bottom{bottom}, left{left}, right{right} {
  subject->attach(this);
}

TextObserver::~TextObserver() { subject->detach(this); }

void TextObserver::notify() {
  std::cout << '+';
  for (int j = left; j < right + 1; ++j)
    std::cout << '-';
  std::cout << '+' << std::endl;
  for (int i = top; i < bottom + 1; ++i) {
    std::cout << '|';
    for (int j = left; j < right + 1; ++j) {
      std::cout << (subject->getState(i, j));
    }
    std::cout << '|' << std::endl;
  }
  std::cout << '+';
  for (int j = left; j < right + 1; ++j)
    std::cout << '-';
  std::cout << '+' << std::endl;
}
