#include <memory>

using namespace std;

class A {
	int x;
};

class B {
	int y;
};

class CImpl {
	A a;
	B b;
};

class C {
private:
	std::unique_ptr<CImpl> impl;

public:
	void f() { std::unique_ptr<CImpl> p = std::make_unique<CImpl>(impl); }
}
