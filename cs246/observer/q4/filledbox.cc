#include "filledbox.h"

FilledBox::FilledBox(int row, int col, char val, AsciiArt *component)
    : Decorator{component}, val{val}, theRow{row}, theCol{col} {}

char FilledBox::charAt(int row, int col, int tick) {
  if (theRow == row && theCol == col) {
    return val;
  } else {
    return component->charAt(row, col, tick);
  }
}
