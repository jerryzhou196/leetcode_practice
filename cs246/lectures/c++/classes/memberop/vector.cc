#include "vector.h"
#include <iostream>

using namespace std;

Vector::Vector(int x, int y): x(x), y(y) {}

Vector Vector::operator+(const Vector &v) const {
  return Vector(x + v.x, y + v.y);
}

Vector Vector::operator*(const int k) const {
  return Vector(k * x, k * y);
}

Vector operator*(const int k, const Vector &v) {
  return v * k;
}

ostream &operator<<(ostream &out, const Vector &v) {
  out <<  "(" << v.x << "," << v.y << ")";
  return out;
}

