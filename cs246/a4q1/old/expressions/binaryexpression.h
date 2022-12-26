#include <string>
#include "expression.h"

enum BinaryOperator { ADD, MINUS, DIVIDE, MULTIPLY };

class BinaryExpression : public Expression {
private:
	Expression*    l;
	Expression*    r;
	BinaryOperator op;

public:  // check if this is even necessary
	BinaryExpression(Expression* l, Expression* r, BinaryOperator op);
	~BinaryExpression();
	void prettyprint() const override;
	bool intialized() const override;
	void set(std::string var, int val) override;
	void unset(std::string var) override;
	int  evaluate() const override;
};
