#include "text.h"
#include <string>

using namespace std;

Text::Text(const string &title, const string &author, int numPages, const string &topic):
  Book{title, author, numPages}, topic{topic} {}

string Text::getTopic() const { return topic; }
