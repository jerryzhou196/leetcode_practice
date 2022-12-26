#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(void) {
	string       nice = "+1";
	stringstream i{nice};

	int x;
	i >> x;
	bool y = i.fail();
	cout << x;

	cout << "nice";
}
