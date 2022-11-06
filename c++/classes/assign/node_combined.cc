#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *next;
  explicit Node(int data, Node *next = nullptr): data{data}, next{next} {}

  Node(const Node &n): data{n.data}, next{n.next ? new Node{*n.next} : nullptr} {}

  ~Node() {
    delete next;
  }

  Node &operator=(const Node &other) {
    if (this == &other) return *this;
    data = other.data;
    Node *tmp = next;
    next = other.next ? new Node(*other.next) : nullptr;
    return *this;
  }
};

ostream &operator<<(ostream &out, const Node &n) {
  out << n.data;
  if (n.next) {
    out << "," << *n.next;
  }
  return out;
}


int main() {
  Node n{1, new Node{2, new Node{3, nullptr}}};

  Node m{4, nullptr};

  m = n;

  cout << n << endl;
  cout << m << endl;

  cout << endl;

  n.next->next->data = 7;

  cout << n << endl;
  cout << m << endl;
}
