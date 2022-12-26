#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

class Obsever {
public:
	virtual void notify() = 0;
	virtual     *Obsever() {}
};

class Subject {
	vector<Obsever *> observers;

public:
	void atttach(Observer *ob) { observers->emplace_back(ob); }
	void detach(Observer *ob){};
	void notifyObservers() {
		for (auto ob : observers) ob->notify();  // auto generated ITERATORS
	}
	virtual ~Subject() = 0;  // DONT FORGET TO IMPLEMENT THIS
}
