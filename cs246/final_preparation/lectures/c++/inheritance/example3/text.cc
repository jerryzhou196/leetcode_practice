#include "text.h"
#include <string>

using std::string;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

bool Text::isItHeavy() const { return getNumPages() > 400; }
string Text::getTopic() const { return topic; }

