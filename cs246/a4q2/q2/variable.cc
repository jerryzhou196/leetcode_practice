#include <iostream>
#include <string>

#include "variable.h"

using namespace std;

Variable::Variable(string name) : name{name}, initalized{false} {}
Variable::Variable(string name, int val) : name{name}, val{val}, initalized{true} {}

string Variable::prettyprint() const {
	return (!initalized) ? name : to_string(val);
};
void Variable::set(string var, int value) {
	if (name == var) {
		initalized = true;
		val        = value;
	}
}
void Variable::unset(string var) {
	if (name == var && initalized) {
		initalized = false;

		// these variables are ideally not necessary, but useful for debugging
		val = -1;
	}
}
int Variable::evaluate() const {
	return val;
	// one NEEDS to check if intialized before calling evluate
}

bool Variable::intialized() const {
	if (!initalized) {
		cout << name << " has no value." << endl;
		return false;
	} else {
		return true;
	}
}

Expression* Variable::get_copy() const {
	Expression* copy = (initalized) ? new Variable(name, val) : new Variable(name);
	return copy;
}
