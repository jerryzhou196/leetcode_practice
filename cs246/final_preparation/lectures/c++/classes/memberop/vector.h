#ifndef __VECTOR_H__
#define __VECTOR_H__
#include <iostream>

struct Vector {
  int x, y;

  explicit Vector(int x = 0, int y = 0);

  Vector operator+(const Vector &v) const;
  Vector operator*(const int k) const;
};

Vector operator*(const int k, const Vector &v);

std::ostream& operator<<(std::ostream &out, const Vector &v);

#endif
