#include "text.h"
#include <string>

using namespace std;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

bool Text::isItHeavy() { return getNumPages() > 400; }
string Text::getTopic() { return topic; }

