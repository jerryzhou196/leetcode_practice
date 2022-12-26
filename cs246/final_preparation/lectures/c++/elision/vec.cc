#include <iostream>
using namespace std;

struct Vec {
  int x, y;
  Vec(int x, int y): x{x}, y{y} {
    cout << "Basic ctor" << endl;
  }
  Vec(const Vec &other): x{other.x}, y{other.y} {
    cout << "Copy ctor" << endl;
  }
  Vec(Vec &&other): x{other.x}, y{other.y} {
    cout << "Move ctor" << endl;
  }
};

Vec makeAVec() { return {0, 0}; }

int main() {
  Vec v = makeAVec();
}
