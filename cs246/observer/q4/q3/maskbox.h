#ifndef _MASKBOX_H_
#define _MASKBOX_H_

#include "asciiart.h"
#include "decorator.h"

class MaskBox : public Decorator {
  char val;
  int theRow;
  int theCol;

public:
  MaskBox(int row, int col, char val, AsciiArt *component);
  char charAt(int row, int col, int tick) override;
};
#endif
