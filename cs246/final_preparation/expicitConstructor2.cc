#include <iostream>
#include <string>

using namespace std;

class Person {
public:
	explicit Person(std::string name, int age, double height, double weight, char gender){

	};

	~Person() { cout << "lmao" << endl; }

private:
	std::string name_;
	int         age_;
	double      height_;
	double      weight_;
	char        gender_;
};

int main() {
	Person p1("John Smith", 30, 1.80, 80.0,
	          'M');  // OK, explicit call to the constructor

	// Person p2 = {"John Smith", 30, 1.80, 80.0, 'M'};  // error, constructor is marked as explicit
}
