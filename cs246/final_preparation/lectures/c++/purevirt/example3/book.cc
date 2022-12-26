#include <iostream>
#include <string>
#include "book.h"

using namespace std;

Book::Book(const string &title, const string &author, int numPages): AbstractBook{title, author, numPages} {}

Book::Book(const Book &b): AbstractBook{b} {}

Book& Book::operator=(const Book &rhs) {
  cout << "Book assignment operator running ..." << endl;

  if (this == &rhs) return *this;
  AbstractBook::operator=(rhs);
  return *this;
}

Book::~Book() {}
