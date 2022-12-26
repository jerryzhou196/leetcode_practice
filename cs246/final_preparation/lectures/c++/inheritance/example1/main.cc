#include <iostream>
#include <string>
#include "book.h"
#include "text.h"
#include "comic.h"

using namespace std;

int main() {
  Book b("War and Peace", "Tolstoy", 5000);
  Text t("Algorithms", "CLRS", 400, "C");
  Comic c("Robin and his Sidekick Batman", "Robin", 20, "Robin");

  cout << "First book: " << b.getTitle() << "; " << b.getAuthor()
       << "; " << (b.isItHeavy() ? "heavy" : "not heavy") << endl;

  cout << "Second book: " << t.getTitle() << "; " << t.getAuthor()
       << "; " << (t.isItHeavy() ? "heavy" : "not heavy") << endl;

  cout << "Third book: " << c.getTitle() << "; " << c.getAuthor()
       << "; " << (c.isItHeavy() ? "heavy" : "not heavy") << endl;
}
