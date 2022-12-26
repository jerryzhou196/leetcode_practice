#include "blinkingbox.h"
#include "decorator.h"

BlinkingBox::BlinkingBox(int row, int col, char val, AsciiArt *component)
    : Decorator{component}, val{val}, theRow{row}, theCol{col} {}

char BlinkingBox::charAt(int row, int col, int tick) {
  if (theRow == row && col == theCol && tick % 2 == 0) {
    return val;
  } else {
    return component->charAt(row, col, tick);
  }
}
