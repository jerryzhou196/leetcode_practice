#include <iostream>
#include <string>

/*
 * PornStars
 * products implement the same interface so that the classes can refer
 * to the interface not the concrete product
 */
class PornStars {
public:
	virtual ~PornStars() {}

	virtual std::string getName() = 0;
	virtual int         getCost() = 0;

	// ...
};

/*
 * Concrete PornStars
 * define product to be created
 */
class Sarah : public PornStars {
public:
	~Sarah() {}
	std::string getName() { return "type A"; }
	int         getCost() { return 1; }
	// ...
};

/*
 * Concrete PornStars
 * define product to be created
 */
class Bob : public PornStars {
public:
	~Bob() {}
	std::string getName() { return "type B"; }
	int         getCost() { return 999; }
	// ...
};

/*
 * Creator
 * contains the implementation for all of the methods
 * to manipulate products except for the factory method
 */
class Creator {
public:
	virtual ~Creator() {}

	virtual PornStars *createBob()   = 0;
	virtual PornStars *createSarah() = 0;

	virtual void removeProduct(PornStars *product) = 0;

	// ...
};

/*
 * Concrete Creator
 * implements factory method that is responsible for creating
 * one or more concrete products ie. it is class that has
 * the knowledge of how to create the products
 */
class PornStarCreator : public Creator {
public:
	~PornStarCreator() {}

	PornStars *createBob() { return new Sarah(); }

	PornStars *createSarah() { return new Bob(); }

	void removeProduct(PornStars *product) { delete product; }
	// ...
};

int main() {
	Creator *creator = new PornStarCreator();

	PornStars *p1 = creator->createBob();
	std::cout << "PornStars: " << p1->getName() << std::endl;
	creator->removeProduct(p1);

	PornStars *p2 = creator->createSarah();
	std::cout << "PornStars: " << p2->getName() << std::endl;
	creator->removeProduct(p2);

	delete creator;
	return 0;
}
