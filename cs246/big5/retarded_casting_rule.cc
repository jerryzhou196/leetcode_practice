#include <iostream>
#include <string>

using namespace std;

struct fake_string {
	int x;
	fake_string(int x);
};

fake_string::fake_string(int x) : x(x) {}

void I_ONLY_ACCEPT_FUCKING_STRINGS_BITCH(fake_string x) {
	cout << x.x;
}

int main(void) {
	I_ONLY_ACCEPT_FUCKING_STRINGS_BITCH(69 + 4);
}
