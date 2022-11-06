#include <iostream>
#include <istream>

using namespace std;

struct ConstRef {
  int i;
  const int ci;
  int &ri;
  ConstRef(int ii, int constant, int &ref); // default constructor?
};

ConstRef::ConstRef(int ii, int constant, int &ref)
    : i(ii), ci(constant), ri(ref) {} // if it were ri(ref), you would instantly
                                      // lose ref after exiting the constructor

struct Screen {
  Screen &clear(char = bkground); // defa
  static const char bkground;
};

struct Foo {
  int balls;
};

int main(void) {

  foo aboutToBeDestructred;

  int x = 699;

  ConstRef balls(1, 2, x);

  cout << balls.ri;

  x = 1251825;
  int nice = 5;

  x = 69;

  return 0;
}
