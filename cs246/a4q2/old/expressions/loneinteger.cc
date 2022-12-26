#include <iostream>
#include <string>

#include "loneinteger.h"

using namespace std;

LoneInteger::LoneInteger(int val) : val{val} {}

void LoneInteger::prettyprint() const {
	cout << val;
};
void LoneInteger::set(string var, int val) {}
void LoneInteger::unset(string var) {}
int  LoneInteger::evaluate() const {
	 return val;
}
bool LoneInteger::intialized() const {
	return true;
}
