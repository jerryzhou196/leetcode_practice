#ifndef BLANK_H
#define BLANK_H

#include "asciiart.h"

class Blank : public AsciiArt {
private:
  char val;

public:
  char charAt(int row, int col, int tick) override;
};

#endif
