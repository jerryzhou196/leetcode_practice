#include <iostream>
#include <stdexcept>

using namespace std;

void f() {
	// throw out_of_range{"f failed"};  // out_of_range is class, {"f failed"} is object constructed
}

void g() {
	f();
}
void h() {
	g();
}

class badInput {};

int main() {
	try {
		h();
	} catch (out_of_range r) {
		cout << "lmao" << endl;
		cout << r.what() << endl;
	}

	try {
		int n;
		if (!(cin >> n)) throw badInput{};
	} catch (badInput&) {             // we can omit the variable name if it's not being used (and the object would be empty anyways)
		cout << "bad input" << endl;  // Note: caught by reference- badInput& - we do so because of polymorphism - whoever is raising the
		                              // exception could be raising a subtype of badInput - so if we catch by reference, it pretens object
		                              // slicing and will let the exception behave as the subtype if virtual methods are overridden
	}

	cout << "please send help im being held hostage" << endl;
}
