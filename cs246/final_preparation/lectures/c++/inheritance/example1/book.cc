#include <string>
#include "book.h"

using namespace std;

Book::Book(const string &title, const string &author, int numPages):
  title{title}, author{author}, numPages{numPages} {}

string Book::getTitle() const { return title; }
string Book::getAuthor() const { return author; }
int Book::getNumPages() const { return numPages; }
bool Book::isItHeavy() const { return numPages > 200; }
