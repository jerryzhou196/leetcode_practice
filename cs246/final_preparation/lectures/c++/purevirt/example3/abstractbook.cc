#include <iostream>
#include <string>
#include "abstractbook.h"

using namespace std;

AbstractBook::AbstractBook(const string &title, const string &author, int numPages):
  title{title}, author{author}, numPages{numPages} {}

AbstractBook::AbstractBook(const AbstractBook &b): title{b.title}, author{b.author}, numPages{b.numPages} {
  cout << "Running the AbstractBook's copy ctor... " << endl;
}

AbstractBook& AbstractBook::operator=(const AbstractBook &rhs) {
  cout << "AbstractBook assignment operator running ..." << endl;

  if (this == &rhs) return *this;
  title = rhs.title;
  author = rhs.author;
  numPages = rhs.numPages;
  return *this;
}

int AbstractBook::getNumPages() const { return numPages; }
string AbstractBook::getTitle() const { return title; }
string AbstractBook::getAuthor() const { return author; }
bool AbstractBook::isItHeavy() const { return numPages > 200; }

// My favourite books are short books.
bool AbstractBook::favourite() const { return numPages < 100; }

AbstractBook::~AbstractBook() {}
