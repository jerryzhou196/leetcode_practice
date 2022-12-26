#include <iostream>

#include "asciiart.h"
#include "blank.h"
#include "studio.h"

#include "blinkingbox.h"
#include "filledbox.h"
#include "maskbox.h"
#include "movingbox.h"

enum paintType { FILL, BLINK, MASK };

void addBox(int row_start, int row_end, int column_start, int column_end,
            char what, AsciiArt *&board, paintType p) {
  for (int x = row_start; x < row_end + 1; x++) {
    for (int y = column_start; y < column_end + 1; y++) {
      switch (p) {
      case FILL:
        board = new FilledBox(x, y, what, board);
        break;
      case BLINK:
        board = new BlinkingBox(x, y, what, board);
        break;
      case MASK:
        board = new MaskBox(x, y, what, board);
        break;
      }
    }
  }
}

int main() {
  AsciiArt *canvas = new Blank;

  Studio s{canvas};

  std::string command;

  while (std::cin >> command) {
    if (command == "render") {
      s.render();
    } else if (command == "animate") {
      int n;
      std::cin >> n;
      s.animate(n);
    } else if (command == "reset") {
      s.reset();
    } else if (command == "filledbox") {
      int top, bottom, left, right;
      char what;
      std::cin >> top >> bottom >> left >> right >> what;
      addBox(top, bottom, left, right, what, s.picture(), FILL);
    } else if (command == "blinkingbox") {
      int top, bottom, left, right;
      char what;
      std::cin >> top >> bottom >> left >> right >> what;
      addBox(top, bottom, left, right, what, s.picture(), BLINK);
    } else if (command == "movingbox") {
      int top, bottom, left, right;
      char what, dir;
      std::cin >> top >> bottom >> left >> right >> what >> dir;
      for (int y = top; y < bottom + 1; y++) {
        for (int x = left; x < right + 1; x++) {
          switch (dir) {
          case 'u':
            s.picture() = new MovingBox(y, x, what, UP, (s.picture()));
            break;
          case 'd':
            s.picture() = new MovingBox(y, x, what, DOWN, (s.picture()));
            break;
          case 'l':
            s.picture() = new MovingBox(y, x, what, LEFT, (s.picture()));
            break;
          case 'r':
            s.picture() = new MovingBox(y, x, what, RIGHT, (s.picture()));
            break;
          default:
            s.picture() = new MovingBox(y, x, what, RIGHT, (s.picture()));
            break;
          }
        }
      }

    } else if (command == "maskbox") {
      int top, bottom, left, right;
      char what;
      std::cin >> top >> bottom >> left >> right >> what;
      addBox(top, bottom, left, right, what, s.picture(), MASK);
    } else if (command == "addtext") {
      int top, bottom, left, right;
      std::cin >> top >> bottom >> left >> right;

    } else if (command == "addgraphics") {
      int top, bottom, left, right;
      std::cin >> top >> bottom >> left >> right;
    }
  }
  delete s.picture();
}
