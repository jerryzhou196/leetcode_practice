#include <iostream>

using namespace std;

class Base {
public:
	int a;  // THIS WAS FREE TO EVERYONE IN THE FIRST PLACE

protected:
	int b;  // THIS IS ONlY FREE TO ITS CHILDREN

private:
	int c;  // THIS IS ITS DEEPEST DARKEST SECRETS
};

class Derived : public Base {  // PUBLIC: doesn't change the given scopes
	                           // a is public
	                           // b is protected
	                           // c is not accessible from Derived
};

class Derived2 : protected Base {  // reduces the PUBLIC property down to PROTECTED
	                               // a is protected
	                               // b is protected
	                               // c is not accessible from Derived2
};

class Derived3 : private Base {
	cout << a << endl;
	// a is private
	// b is private
	// c is not accessible from Derived3
};

int main(void) {
	Base a;
	a.a = 69;

	Base Derived1;
}
