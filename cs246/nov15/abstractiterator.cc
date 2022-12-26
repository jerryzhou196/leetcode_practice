#include <iostream>
#include <stdexcept>

using namespace std;

// Iterator Pattern 🥺

class AbstractIterator {
public:
	virtual int &operator*()                                     = 0;
	virtual int &operator++()                                    = 0;
	virtual int &operator!=(const AbstractIterator &other) const = 0;
	virtual ~AbstractIterator() {}
};

class List {
public:
	class Iterator : public AbstractIterator {};
};

// Why is this significant?
// Because we can use this AbstractIterator for all kinds of ADTs

class Set {
public:
	class SetIterator : AbstractIterator {};
};

// this generalizes the for each looop
void for_each(AbstractIterator &start, AbstractIterator &finish, int (*f)(int)) {
	while (start != finish) {
		f(*start);
		++start;
	}
}
