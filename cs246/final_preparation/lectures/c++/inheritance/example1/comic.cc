#include "comic.h"
#include <string>

using std::string;

Comic::Comic(const string &title, const string &author, int numPages, const string &hero):
  Book{title, author, numPages}, hero{hero} {}

string Comic::getHero() const { return hero; }

