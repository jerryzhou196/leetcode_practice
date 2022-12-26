
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "binaryexpression.h"
#include "expression.h"
#include "loneinteger.h"
#include "unaryexpression.h"
#include "variable.h"

using namespace std;

void handleBinary(vector<Expression*>& estack, BinaryOperator op) {
	int n = estack.size();
	if (n < 2) return;  // not big enough

	Expression* s = new BinaryExpression(estack[n - 2], estack[n - 1], op);
	estack.erase(estack.begin() + n - 1);
	estack.erase(estack.begin() + n - 2);
	estack.push_back(s);
}

void handleUnary(vector<Expression*>& estack, UnaryOperator op) {
	int n = estack.size();
	if (n < 1) return;

	Expression* s = new UnaryExpression(estack[n - 1], op);
	estack[n - 1] = s;  // this is sussy - we might prefer to use the ERASE method still
}

int main(void) {
	string              input;
	vector<Expression*> estack;

	while (cin >> input) {
		int           x;
		istringstream s{input};
		s >> x;

		if (s.fail()) {
			switch (input[0]) {
				case '+': handleBinary(estack, ADD); continue;
				case '-': handleBinary(estack, MINUS); continue;
				case '/': handleBinary(estack, DIVIDE); continue;
				case '*': handleBinary(estack, MULTIPLY); continue;
				default: break;
			}

			if (input == "ABS") {
				handleUnary(estack, ABS);
				continue;
			}

			if (input == "NEG") {
				handleUnary(estack, NEG);
				continue;
			}

			if (input == "done") {
				cout << estack[estack.size() - 1]->prettyprint() << endl;
				break;
			}

			Expression* s = new Variable(input);
			estack.push_back(s);
		} else {
			Expression* s = new LoneInteger(x);
			estack.push_back(s);
		}
	}

	while (cin >> input) {
		int         n = estack.size();
		Expression* e = estack[n - 1];

		if (input == "eval" && e->intialized()) cout << e->evaluate() << endl;

		if (input == "set") {
			string var;
			int    val;
			cin >> var >> val;
			if (!cin.fail()) e->set(var, val);
		}

		if (input == "unset" && e->intialized()) {
			string var;
			cin >> var;
			if (!cin.fail()) e->unset(var);
		}

		if (input == "print" && e->intialized()) {
			cout << e->prettyprint() << endl;
		}

		if (input == "copy") {
			Expression* theCopy = e->get_copy();
			cout << theCopy->prettyprint() << endl;
			theCopy->set("x", 1);
			cout << theCopy->prettyprint() << endl;
			if (theCopy->intialized()) cout << theCopy->evaluate() << endl;
			delete theCopy;
		}
	}

	int n = estack.size();
	for (int x = 0; x < n; x++) delete estack[x];
	return 0;
}
