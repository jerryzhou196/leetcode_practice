#include <iostream>

#include "asciiart.h"
#include "blank.h"
#include "studio.h"

#include "blinkingbox.h"
#include "filledbox.h"
#include "maskbox.h"
#include "movingbox.h"

#include "graphicobserver.h"
#include "textobserver.h"

#include "window.h"

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

  std::vector<Observer *> history;
  // Create a Subject class
  // Handle adding observers in the addText and addGraphics

  std::string command;

  while (std::cin >> command) {
    if (command == "render") {
      s.runRender();
    } else if (command == "addshit") {

    } else if (command == "addtext") {
      int top, bottom, left, right;
      std::cin >> top >> bottom >> left >> right;
      TextObserver *t = new TextObserver(&s, top, bottom, left, right);
      // add Text Observer
    } else if (command == "addgraphics") {

      int top, bottom, left, right;
      std::cin >> top >> bottom >> left >> right;
      GraphicObserver *g = new GraphicObserver(&s, top, bottom, left, right);
    }
  }
  delete s.picture();
}
