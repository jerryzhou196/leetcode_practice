#include <iostream>
using namespace std;
#define DEBUG 69

int main() {
#ifndef DEBUG
	cout << "setting x=1" << endl;
#endif
	int x = 1;
	while (x < 10) {
		++x;
#ifdef DEBUG
		cout << "x is now " << x << endl;
#endif
	}
	cout << x << endl;
}
