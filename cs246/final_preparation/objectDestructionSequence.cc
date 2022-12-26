#include <iostream>
#include <string>
using namespace std;

// FIRST - space is allocated
// SECOND - superclass portfion of the constructor is run
// THIRD - fields in MIl are

class Book {
protected:
	string text;
	int    length;

public:
	explicit Book(string text = "", int length = 0) : text{text}, length{length} {}  // default constructor no longer exists
};

class AdultMagazine : protected Book {
	string genre;

public:
	AdultMagazine(string genre) : genre{genre} { cout << text << length << endl; }
};

int main(void) {
	Book          b("mein kampf", 500);
	AdultMagazine b1{"hentai"};
	return 0;
}
