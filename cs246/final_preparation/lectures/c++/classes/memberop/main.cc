#include <iostream>
#include "vector.h"

using namespace std;

int main() {
  Vector v1(1,2);
  Vector v2 = v1 + v1;
  Vector v3 = 3 * v2;
  Vector v4 = v1 * 5;

  cout << v1 << " " << v2 << " " << v3 << " " << v4 << endl;
}
