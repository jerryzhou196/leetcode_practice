#include <iostream>
#include <string>

#include "loneinteger.h"

using namespace std;

LoneInteger::LoneInteger(int val) : val{val} {}

string LoneInteger::prettyprint() const {
	return to_string(val);
};
void LoneInteger::set(string var, int val) {}
void LoneInteger::unset(string var) {}
int  LoneInteger::evaluate() const {
	 return val;
}
bool LoneInteger::intialized() const {
	return true;
}

Expression* LoneInteger::get_copy() const {
	Expression* copy = new LoneInteger(val);
	return copy;
}
