#include <iostream>
#include <string>

#include "variable.h"

using namespace std;

Variable::Variable(string name) : name{name}, initalized{false} {}

void Variable::prettyprint() const {
	if (!initalized) {
		cout << name;
	} else {
		cout << val;
	}
};
void Variable::set(string var, int value) {
	initalized = true;
	name       = var;
	val        = value;
}
void Variable::unset(string var) {
	if (name == var && initalized) {
		initalized = false;

		// these variables are ideally not necessary, but useful for debugging
		val  = -1;
		name = "";
	}
}
int Variable::evaluate() const {
	// one NEEDS to check if intialized before calling evluate
	return val;
}

bool Variable::intialized() const {
	if (!initalized) {
		cout << name << " has no value." << endl;
		return false;
	} else {
		return true;
	}
}
