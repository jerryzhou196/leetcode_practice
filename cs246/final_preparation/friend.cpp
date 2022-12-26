#include <iostream>

using namespace std;

class A {
private:
	int x;
	int y;

public:
	A(int x, int y) : y(x), x(y) {}
	friend class B;
};

class B {
public:
	static int sum(A &a) { cout << a.x << a.y << endl; }
};

int main(void) {
	B hi;
	A instance{9, 6};
	A instance1(9, 6);
	hi.sum(instance);
	hi.sum(instance1);
}
