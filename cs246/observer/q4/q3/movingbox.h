#ifndef _MOVINGBOX_H_
#define _MOVINGBOX_H_

#include "asciiart.h"
#include "decorator.h"

enum Direction { UP, DOWN, LEFT, RIGHT };

class MovingBox : public Decorator {
  char val;
  int theRow;
  int theCol;
  Direction dir;

public:
  MovingBox(int row, int col, char val, Direction dir, AsciiArt *component);
  char charAt(int row, int col, int tick) override;
};
#endif
