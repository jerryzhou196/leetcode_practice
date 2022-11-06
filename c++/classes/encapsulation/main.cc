#include <iostream>
#include "list.h"
using namespace std;

class List {
  class Node;
  Node *theList = nullptr;

public:
  void addToFront(int n);
  int ith(int i);
  ~List();
};

List::~List() { delete theList; }

void List::addToFront(int n) { theList = new Node(n, theList); }

int List::ith(int i) {
  Node *cur = theList;
  for (int j = 0; j < i && cur; ++j, cur = cur->next)
    ;
  return cur->data;
}

struct List::Node {
  int data;
  Node *next;

  Node(int data, Node *next) : data{data}, next{next} {}
  ~Node() { delete next; }
};



  int main() {
    List l;
    l.addToFront(1);
    l.addToFront(2);
    l.addToFront(3);

    for (int i = 0; i < 3; ++i) {
      cout << l.ith(i) << endl;
    }
  }
