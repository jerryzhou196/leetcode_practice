#include <iostream>
#include <string>

#include "binaryexpression.h"

using namespace std;

int computeBinary(int x, int y, BinaryOperator op) {
	switch (op) {
		case ADD: return x + y; break;
		case MULTIPLY: return x * y; break;
		case MINUS: return x - y;
		case DIVIDE: return x / y;
	}
}

BinaryExpression::BinaryExpression(Expression* l, Expression* r, BinaryOperator op) : l{l}, r{r}, op{op} {}
BinaryExpression::~BinaryExpression() {
	delete l;
	delete r;
}

string BinaryExpression::prettyprint() const {
	string oper;
	switch (op) {
		case ADD: oper = '+'; break;
		case MINUS: oper = '-'; break;
		case DIVIDE: oper = '/'; break;
		case MULTIPLY: oper = '*'; break;
	}
	return "(" + l->prettyprint() + " " + oper + " " + r->prettyprint() + ")";
};

void BinaryExpression::set(string var, int val) {
	// assumes that var and val are valid
	l->set(var, val);
	r->set(var, val);
}

void BinaryExpression::unset(string var) {
	l->unset(var);
	r->unset(var);
}

int BinaryExpression::evaluate() const {
	return computeBinary(l->evaluate(), r->evaluate(), op);
}
bool BinaryExpression::intialized() const {
	return l->intialized() && r->intialized();
}

Expression* BinaryExpression::get_copy() const {
	Expression* copy = new BinaryExpression(l->get_copy(), r->get_copy(), op);
	return copy;
}
