#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "expression.h"

using namespace std;

enum BinaryOperator { ADD, MINUS, DIVIDE, MULTIPLY };
enum UnaryOperator { ABS, NEG };

int computeBinary(int x, int y, BinaryOperator op) {
	switch (op) {
		case ADD: return x + y; break;
		case MULTIPLY: return x * y; break;
		case MINUS: return x - y;
		case DIVIDE: return x / y;
	}
}

int abs(int x) {
	return (x < 0) ? -1 * x : x;
}

int computeUnary(int x, UnaryOperator op) {
	switch (op) {
		case ABS: return abs(x); break;
		case NEG: return -1 * x; break;
	}
}

class BinaryExpression : public Expression {
private:
	Expression*    l;
	Expression*    r;
	BinaryOperator op;

public:  // check if this is even necessary
	BinaryExpression(Expression* l, Expression* r, BinaryOperator op) : l{l}, r{r}, op{op} {}
	~BinaryExpression() {
		delete l;
		delete r;
	}

	void prettyprint() const override {
		string oper;
		switch (op) {
			case ADD: oper = '+'; break;
			case MINUS: oper = '-'; break;
			case DIVIDE: oper = '/'; break;
			case MULTIPLY: oper = '*'; break;
		}

		cout << "(";
		l->prettyprint();
		cout << " ";
		cout << oper;
		cout << " ";
		r->prettyprint();
		cout << ")";
	};
	void set(string var, int val) override {
		// assumes that var and val are valid
		l->set(var, val);
		r->set(var, val);
	}
	void unset(string var) override {
		l->unset(var);
		r->unset(var);
	}
	int  evaluate() const override { return computeBinary(l->evaluate(), r->evaluate(), op); }
	bool intialized() const override { return l->intialized() && r->intialized(); }
};

class UnaryExpression : public Expression {
private:
	Expression*   e;
	UnaryOperator op;

public:  // check if this is even necessary
	UnaryExpression(Expression* e, UnaryOperator op) : e{e}, op{op} {}
	~UnaryExpression() { delete e; }

	void prettyprint() const override {
		if (op == ABS) {
			cout << "|";
			e->prettyprint();
			cout << "|";
		} else {
			cout << "-";
			e->prettyprint();
		}
	};

	void set(string var, int val) override { e->set(var, val); }

	void unset(string var) override { e->unset(var); }

	int evaluate() const override { return computeUnary(e->evaluate(), op); }

	bool intialized() const override { return e->intialized(); }
};

class LoneInteger : public Expression {
private:
	int val;

public:  // check if this is even necessary
	LoneInteger(int val) : val{val} {}
	void prettyprint() const override { cout << val; };
	void set(string var, int val) override {}
	void unset(string var) override {}
	int  evaluate() const override { return val; }
	bool intialized() const override { return true; }
};

class Variable : public Expression {
private:
	string name;
	int    val;
	bool   initalized;

public:  // check if this is even necessary
	Variable(string name) : name{name}, initalized{false} {}
	void prettyprint() const override {
		if (!initalized) {
			cout << name;
		} else {
			cout << val;
		}
	};
	void set(string var, int value) override {
		initalized = true;
		name       = var;
		val        = value;
	}
	void unset(string var) override {
		if (name == var && initalized) {
			initalized = false;

			// these variables are ideally not necessary, but useful for debugging
			val  = -1;
			name = "";
		}
	}
	int evaluate() const override {
		// one NEEDS to check if intialized before calling evluate
		return val;
	}

	bool intialized() const override {
		if (!initalized) {
			cout << name << " has no value." << endl;
			return false;
		} else {
			return true;
		}
	}
};

// returns
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
	string input;

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
				estack[estack.size() - 1]->prettyprint();
				cout << endl;
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
		int n = estack.size();
		if (input == "eval" && estack[n - 1]->intialized()) cout << estack[n - 1]->evaluate() << endl;

		if (input == "set") {
			string var;
			int    val;
			cin >> var >> val;
			if (!cin.fail()) estack[n - 1]->set(var, val);
		}

		if (input == "unset" && estack[n - 1]->intialized()) {
			string var;
			cin >> var;
			if (!cin.fail()) estack[n - 1]->unset(var);
		}
	}

	int n = estack.size();
	for (int x = 0; x < n; x++) delete estack[x];
	return 0;
}
