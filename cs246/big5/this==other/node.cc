#include "node.h"
#include <iostream>
using namespace std;

ostream &operator<<(ostream &out, const Node &n) {
	out << n.data;
	if (n.next) {
		out << "," << *n.next;
	}
	return out;
}
