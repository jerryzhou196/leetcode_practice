#include "maskbox.h"

MaskBox::MaskBox(int row, int col, char val, AsciiArt *component)
    : Decorator{component}, val{val}, theRow{row}, theCol{col} {}

char MaskBox::charAt(int row, int col, int tick) {
  if (theRow == row && theCol == col &&
      component->charAt(row, col, tick) != ' ') {
    return val;
  } else if (theRow != row || theCol != col) {
    return component->charAt(row, col, tick);
  } else {
    return ' ';
  }
}
