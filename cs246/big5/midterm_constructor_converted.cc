#include <iostream>

using namespace std;

struct Node {
	int   data;
	Node *next;
	Node(int data, Node *next);
};

Node::Node(int data, Node *next = nullptr) : data{data}, next{next} {}

void foop(int i) {}  // does something with the int} void foo(Node n){ //does something with the Node}
void foo(Node n) {
	cout << n.data;

}  // does something with the Node}

int main() {
	foo(69);
}
