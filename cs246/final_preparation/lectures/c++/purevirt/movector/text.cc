#include <iostream>
#include "text.h"
#include <string>
#include <utility>

using namespace std;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

bool Text::isItHeavy() const { return getNumPages() > 500; }
string Text::getTopic() const { return topic; }

// My favourite textbooks are C++ books
bool Text::favourite() const { return topic == "C++"; }

Text::Text(Text &&other): Book{std::move(other)}, topic{std::move(other.topic)} {
  cout << "Running Text's move ctor..." << endl;
}
