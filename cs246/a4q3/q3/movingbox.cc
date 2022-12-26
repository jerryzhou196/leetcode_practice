#include "movingbox.h"

MovingBox::MovingBox(int row, int col, char val, Direction dir,
                     AsciiArt *component)
    : Decorator{component}, val{val}, theRow{row}, theCol{col}, dir{dir} {}

char MovingBox::charAt(int row, int col, int tick) {
  int cur_row = theRow;
  int cur_col = theCol;

  for (int x = 0; x < tick; x++) {
    switch (dir) {
    case UP:
      --cur_row;
      break;
    case DOWN:
      ++cur_row;
      break;
    case LEFT:
      --cur_col;
      break;
    case RIGHT:
      ++cur_col;
      break;
    }
  }
  if (row == cur_row && col == cur_col) {
    return val;
  } else {
    return component->charAt(row, col, tick);
  }
};
