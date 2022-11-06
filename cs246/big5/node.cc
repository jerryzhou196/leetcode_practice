#include <iostream>
using namespace std;

int terrible_global_variable = 0;

struct Node {
	int   val  = 0;
	Node* next = nullptr;
	Node() : {}
};

int main(void) {
	Node n;
}
