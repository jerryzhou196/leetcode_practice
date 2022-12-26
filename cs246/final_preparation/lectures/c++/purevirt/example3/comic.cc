#include "comic.h"
#include <iostream>
#include <string>

using namespace std;

Comic::Comic(const string &title, const string &author, int numPages, const string &hero):
  AbstractBook{title, author, numPages}, hero{hero} {}

Comic::Comic(const Comic &c): AbstractBook{c}, hero{c.hero} {}

Comic& Comic::operator=(const Comic &rhs) {
  cout << "Comic assignment operator running ..." << endl;
  if (this == &rhs) return *this;
  AbstractBook::operator=(rhs);
  hero = rhs.hero;
  return *this;
}

bool Comic::isItHeavy() const { return getNumPages() > 30; }
string Comic::getHero() const { return hero; }

// My favourite comic books are Superman comics.
bool Comic::favourite() const { return hero == "Superman"; }
