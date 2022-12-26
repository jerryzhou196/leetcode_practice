#include <iostream>
#include <cmath>
using namespace std;

class Vec {
 public:
  int x, y;
  Vec(int x, int y): x{x}, y{y} {}
  int supNorm() { return max(abs(x), abs(y)); }
};

class Vec2 {
 public:
  int x, y;
  Vec2(int x, int y): x{x}, y{y} {}
  virtual int supNorm() { return max(abs(x), abs(y)); }
};

int main() {
  Vec v{1,2};
  Vec2 w{1,2};

  cout << sizeof(v) << " " << sizeof(w) << endl;
}
