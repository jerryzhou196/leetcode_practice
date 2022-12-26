#include <iostream>
#include "text.h"
#include <string>

using namespace std;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

bool Text::isItHeavy() const { return getNumPages() > 500; }
string Text::getTopic() const { return topic; }

// My favourite textbooks are C++ books
bool Text::favourite() const { return topic == "C++"; }

Text::Text(const Text &other): Book{other}, topic{other.topic} {
  cout << "Running Text's copy ctor..." << endl;
}
