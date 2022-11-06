#include <iostream>
#include <string>
#include "gokart.h"

std::ostream& operator<<(std::ostream& out, const GoKart& kart) {
	const char* direction[] = {"north", "east", "south", "west"};
	out << kart.driverName() << "'s kart at (" << kart.location().ew << "," << kart.location().ns << ") facing " << direction[kart.facing()]
	    << " at " << kart.speed() << " u/s drove " << kart.distance() << " meters and was hit by " << kart.shellHits() << " blue shells.";
	return out;
}

using namespace std;

int main() {
	string name;
	cout << "Enter name of driver:" << endl;
	cin >> name;

	GoKart k(name);
	char   command;

	cout << "Enter command:" << endl;
	while (cin >> command) {
		if (command == 'a') {
			int a = 0;
			cin >> a;
			k.accelerate(a);
		} else if (command == 'l') {
			k.left();
		} else if (command == 'r') {
			k.right();
		} else if (command == 's') {
			k.step();
		} else if (command == 'p') {
			cout << k << endl;
		} else if (command == 'b') {
			k.blueshell();
		}
		cout << "Enter command:" << endl;
	}
	return 0;
}
