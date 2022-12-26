#include <iostream>
#include <string>
using namespace std;

// Want to enhance an object at runtime - add functionality/functions

// Eg. Windowing system - start with a basic Window,
//					   - add a scrollbar
// 					   - add a menu
// But we want to implement this without an explosion of exponentially increasing components

class Pizza {
public:
	virtual float  price() const = 0;
	virtual string desc() const  = 0;
	virtual ~Pizza(){};
};

class CrustAndSauce : public Pizza {
public:
	float  price() const override { return 5.99; };
	string desc() const override { return "pizza"; }
};

// nobody shows up to his fucking stupid pizzaria. what's wrong?
// so he will hire a UWaterloo CS coop student

// QUESTION 3 on the assignment does THIS

class Decorator : public Pizza {
protected:
	Pizza* component;

public:
	Decorator(Pizza* p) : component{p} {};
	~Decorator() { delete component; };
};

// It's a choice whether or not you want this to be a "has a" or a "owns a"
// it depends on whether or not you think if you remove one object, you need to remove the other

// in this case, if you destroy the pizza in this case, you also destroy the toppings
// but in the window case, if you destroy the scrollbar, you shouldn't also delete the other GUI components

class StuffedCrust : public Decorator {
public:
	StuffedCrust(Pizza* p) : Decorator{p};
	float price() const override { return 2.69 + component->price(); };
};

class Topping : public Decorator {
	string theTopping;

public:
	Topping(string topping, Pizza* p) : Decorator{p}, theTopping{topping} {};
	float  price() const override { return component->price() + 0.75; };
	string desc() const override { return component->desc() + "with" + theTopping; };
};

int main(void) {
	Pizza* p1 = new CrustAndSauce();
	p1        = new Topping{"Cheese", p1};
	p1        = new Topping{"Mushroom", p1};
	p1        = new StuffedCrust{p1};

	cout << p1->desc() << p1->price() << endl;
}
