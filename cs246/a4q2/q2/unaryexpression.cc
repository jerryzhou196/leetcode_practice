
#include <iostream>
#include <string>

#include "unaryexpression.h"

using namespace std;

int abs(int x) {
	return (x < 0) ? -1 * x : x;
}

int computeUnary(int x, UnaryOperator op) {
	switch (op) {
		case ABS: return abs(x); break;
		case NEG: return -1 * x; break;
	}
}

UnaryExpression::UnaryExpression(Expression* e, UnaryOperator op) : e{e}, op{op} {}
UnaryExpression::~UnaryExpression() {
	delete e;
}

string UnaryExpression::prettyprint() const {
	if (op == ABS) {
		return "|" + e->prettyprint() + "|";
	} else {
		return "-" + e->prettyprint();
	}
};

void UnaryExpression::set(string var, int val) {
	e->set(var, val);
}

void UnaryExpression::unset(string var) {
	e->unset(var);
}

int UnaryExpression::evaluate() const {
	return computeUnary(e->evaluate(), op);
}

bool UnaryExpression::intialized() const {
	return e->intialized();
}

Expression* UnaryExpression::get_copy() const {
	Expression* copy = new UnaryExpression(e->get_copy(), op);
	return copy;
}
