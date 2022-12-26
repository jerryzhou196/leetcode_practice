#ifndef STUDIO_H
#define STUDIO_H
#include <iostream>
class AsciiArt;

#include "subject.h"

class Studio : public Subject {
  int rows = 10, cols = 10, ticks = 0;
  std::ostream &out = std::cout;

  AsciiArt *thePicture;

public:
  explicit Studio(AsciiArt *picture) : thePicture{picture} {}
  void runRender();
  void runAnimate(int n);

  AsciiArt *&picture() { return thePicture; }
  void reset();
  // void render();
  // void animate(int numTicks);
  char getState(int row, int col) const override;
  ~Studio();
};

#endif
