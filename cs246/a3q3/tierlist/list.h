#ifndef LIST_H
#define LIST_H

#include "list.h"

#include <string>

class List {
  /**
   * A a plain-old-data Node class.
   * DO NOT MODIFY THIS CLASS
   */
  struct Node {
    Node *next;
    std::string value;
  };

private:
  size_t n;
  int cur;
  Node *head;

  friend class iterator;
  Node *copy_node(Node *other);
  void swap(List &other);

public:
  class iterator {
  private:
    friend class List;
    Node *cur;
    iterator(Node *p = nullptr);

  public:
    iterator &operator++();

    const std::string &operator*() const;
    bool operator==(const iterator &other) const;
    bool operator!=(const iterator &other) const;
  };

public:
  // Default constructor and destructor.
  // Should initialize new Lists to be empty in constant time.
  List();
  ~List();

  // Copy and move constructors.
  // Copy should run in O(n) time, move in constant time.
  List(List &&other);
  List(const List &other);

  // Copy and move assignment operators.
  // Copy should run in O(n) time, move
  // in constant time.
  List &operator=(const List &other);
  List &operator=(List &&other);

  iterator begin() const;
  iterator end() const;

  // Inserts an element to the front of the list,
  // in constant time.
  void push_front(const std::string &value);

  // Removes an element from the front of the list,
  // if the list is non-empty.  Does nothing if the list
  // is empty.
  void pop_front();

  // Returns the size of the list, in constant time.
  size_t size() const;
};

#endif
