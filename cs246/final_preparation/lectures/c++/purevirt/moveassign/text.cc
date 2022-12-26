#include <iostream>
#include "text.h"
#include <string>
#include <utility>

using namespace std;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

bool Text::isItHeavy() const { return getNumPages() > 400; }
string Text::getTopic() const { return topic; }

// My favourite textbooks are C++ books
bool Text::favourite() const { return topic == "C++"; }

Text::Text(const Text &other): Book{other}, topic{other.topic} {
  cout << "Running Text's copy ctor..." << endl;
}

Text &Text::operator=(Text &&rhs) {
  cout << "Text move assignment operator running ... " << endl;

  if (this == &rhs) return *this;
  Book::operator=(std::move(rhs));
  topic = std::move(rhs.topic);
  return *this;
}
