#ifndef _BLINKINGBOX_H_
#define _BLINKINGBOX_H_

#include "asciiart.h"
#include "decorator.h"

class BlinkingBox : public Decorator {
  char val;
  const int theRow;
  const int theCol;

public:
  BlinkingBox(int row, int col, char val, AsciiArt *component);
  char charAt(int row, int col, int tick) override;
};
#endif
