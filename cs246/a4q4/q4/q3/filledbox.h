#ifndef _FILLEDBOX_H_
#define _FILLEDBOX_H_

#include "asciiart.h"
#include "decorator.h"

class FilledBox : public Decorator {
  char val;
  int theRow;
  int theCol;

public:
  FilledBox(int row, int col, char val, AsciiArt *component);
  char charAt(int row, int col, int tick) override;
};
#endif
