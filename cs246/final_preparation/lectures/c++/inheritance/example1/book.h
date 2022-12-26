#ifndef _BOOK_H_
#define _BOOK_H_
#include <string>

class Book {
  std::string title, author;
  int numPages;
 public:
  Book(const std::string &title, const std::string &author, int numPages);
  std::string getTitle() const;
  std::string getAuthor() const;
  int getNumPages() const;
  bool isItHeavy() const;
};

#endif
