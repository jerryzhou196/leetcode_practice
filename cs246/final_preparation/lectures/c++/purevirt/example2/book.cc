#include <iostream>
#include <string>
#include "book.h"

using namespace std;

Book::Book(const string &title, const string &author, int numPages):
  title{title}, author{author}, numPages{numPages} {}

Book::Book(const Book &b): title{b.title}, author{b.author}, numPages{b.numPages} {
  cout << "Running Book's copy ctor... " << endl;
}

Book& Book::operator=(const Book &rhs) {
  cout << "Book assignment operator running ..." << endl;

  if (this == &rhs) return *this;
  title = rhs.title;
  author = rhs.author;
  numPages = rhs.numPages;
  return *this;
}

int Book::getNumPages() const { return numPages; }
string Book::getTitle() const { return title; }
string Book::getAuthor() const { return author; }
bool Book::isItHeavy() const { return numPages > 200; }

// My favourite books are short books.
bool Book::favourite() const { return numPages < 100; }
