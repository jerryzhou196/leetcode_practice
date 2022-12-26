#include <string>
#include "book.h"

using std::string;

Book::Book(const string &title, const string &author, int numPages):
  title{title}, author{author}, numPages{numPages} {}

int Book::getNumPages() const { return numPages; }
string Book::getTitle() const { return title; }
string Book::getAuthor() const { return author; }
bool Book::isItHeavy() const { return numPages > 200; }

// My favourite books are short books.
bool Book::favourite() const { return numPages < 100; }
