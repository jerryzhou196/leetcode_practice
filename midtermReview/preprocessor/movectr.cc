#include <iostream>
using namespace std;

struct Node {
	int   data;
	Node *next;

	Node(int data, Node *next) : data{data}, next{next} { 
        cout << "Basic ctor" << endl; 
    } 

	Node(const Node &other) : data{other.data}, next{other.next ? new Node{*other.next} : nullptr} { //straght up actually copies each node seperately 
        cout << "Copy ctor" << endl; 
        }


	Node(Node &&other) : data{other.data}, next{other.next} {
		other.next = nullptr; //decapitates other
		cout << "Move ctor" << endl;

        //when we leave this scope, other's destructor is run since we are leaving the scope
	}
	~Node() { delete next; }
};

Node plusOne(Node n) {
	for (Node *p{&n}; p; p = p->next) {
		++p->data;
	}
	return n;
}

ostream &operator<<(ostream &out, const Node &n) {
	out << n.data;
	if (n.next) out << ' ' << *n.next;
	return out;
}

int main() {
	Node n{1, new Node{2, nullptr}};

	Node n2{plusOne(n)}; //returns a rvalue Node that is moved instead of copied

	cout << n << endl << n2 << endl;
}
