#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *next;
  explicit Node(int data, Node *next = nullptr);
  Node(const Node &n);

  ~Node();
  Node &operator=(const Node &other);
  void swap(Node &other);
};

Node::Node(int data, Node *next): data{data}, next{next} {}

Node::Node(const Node &n):
  data{n.data},
  next{n.next ? new Node{*n.next} : nullptr} {}

Node::~Node() {
  delete next;
}

void Node::swap(Node &other) {
  int tmpdata = data;
  data = other.data;
  other.data = tmpdata;

  Node *tmpnext = next;
  next = other.next;
  other.next = tmpnext;
}

Node &Node::operator=(const Node &other) {
  Node tmp = other;
  swap(tmp);
  return *this;
}

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

  n = n;

  cout << n << endl;
  cout << m << endl;

  cout << endl;

  n.next->next->data = 7;

  cout << n << endl;
  cout << m << endl;
}
