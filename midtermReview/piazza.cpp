#include <iostream>

using namespace std;

struct B {
	int n;
};

struct A {
	int n;
	B   nxt;
	A(A& a);
	A(int, B);
	A(A&& a);
};

A::A(A& a) {
	cout << "cpy cotr" << endl;
	this->n   = a.n;
	this->nxt = a.nxt;
}

A::A(int n, B nxt) {
	cout << "def ctor" << endl;
	this->n   = n;
	this->nxt = nxt;
}

A::A(A&& a) {
	cout << "move ctor" << endl;
}

A ret() {
	A a{1, B{2}};
	a.n = 3;
	cout << "created" << endl;
	return a;
}

int main() {
	A a = ret();
	cout << "bar" << endl;
	A a2 = a;
	return 0;
}
