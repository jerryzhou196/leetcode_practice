#include <iostream>
#include <utility>

using namespace std;

struct Yakuza {
	Yakuza* subordinates[5];
	string  name;
	string  title;
	int     numSubords;

	Yakuza(string name, string title);
	~Yakuza();
	Yakuza(Yakuza&& other);
	Yakuza(const Yakuza& other);
	Yakuza& operator=(const Yakuza& other);
	Yakuza& operator=(Yakuza&& other);

	void swap(Yakuza& other);
	bool add(string name, string title);
	bool remove(string name);
	void setTitle(string newTitle);
};

void Yakuza::swap(Yakuza& other) {
	using std::swap;
	swap(name, other.name);
	swap(title, other.title);
	swap(subordinates, other.subordinates);
	swap(numSubords, other.numSubords);
}

Yakuza::Yakuza(string name, string title) : name{name}, title{title}, numSubords{0} {
	for (int i = 0; i < 5; i++) {
		subordinates[i] = nullptr;
	}
}

Yakuza::~Yakuza() {
	for (int i = 0; i < numSubords; i++) {
		delete subordinates[i];
	}
}

Yakuza::Yakuza(Yakuza&& other) : name{other.name}, title{other.title}, numSubords{other.numSubords} {
	for (int i = 0; i < numSubords; i++) {
		subordinates[i]       = other.subordinates[i];
		other.subordinates[i] = nullptr;
	}
}

Yakuza::Yakuza(const Yakuza& other) : name{other.name}, title{other.title}, numSubords{other.numSubords} {
	for (int i = 0; i < numSubords; i++) {
		subordinates[i] = new Yakuza{*other.subordinates[i]};
	}
}
Yakuza& Yakuza::operator=(const Yakuza& other) {
	Yakuza temp = other;
	swap(temp);
	return *this;
}

Yakuza& Yakuza::operator=(Yakuza&& other) {
	swap(other);
	return *this;
}

ostream& operator<<(ostream& out, const Yakuza& y) {
	out << y.name << ", " << y.title;
	for (int i = 0; i < y.numSubords; ++i) {
		out << endl << *y.subordinates[i];
	}
	return out;
}  // operator<<

bool Yakuza::add(string name, string title = "chimpira") {
	if (numSubords > 5) {
		cout << "You cannot have any more subordinates!" << endl;
		return false;
	}

	subordinates[numSubords] = new Yakuza{name, title};
	numSubords++;

	return true;
}

bool Yakuza::remove(string name) {
	for (int i = 0; i < numSubords; i++) {
		if (subordinates[i]->name == name) {
			delete subordinates[i];
			return true;
		}
	}
	return false;
}

void Yakuza::setTitle(string newTitle) {
	title = newTitle;
}

int main() {
	Yakuza majima{"Goro Majima", "Lord of the Night"};
	majima.add("Nishida");
	majima.add("Daisaku Minami");
	majima.add("Ryota Kawamura");
	majima.add("Gary \"Buster\" Holmes", "King of the Ring");

	Yakuza majimaShadowClone{majima};
	cout << "Copy Constructor" << endl;
	cout << majimaShadowClone << endl << endl;

	Yakuza moveMajima = std::move(majimaShadowClone);  // Function to force move constructor
	cout << "Move Constructor" << endl;
	cout << moveMajima << endl << endl;

	majimaShadowClone = std::move(moveMajima);
	cout << "Move Assignment" << endl;
	cout << majimaShadowClone << endl << endl;

	majima.setTitle("Mad Dog of Shimano");
	majimaShadowClone = majima;
	cout << "Copy Assignment" << endl;
	cout << majimaShadowClone << endl << endl;
}
