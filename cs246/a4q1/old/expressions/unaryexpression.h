#include <string>
#include "expression.h"

enum UnaryOperator { ABS, NEG };

class UnaryExpression : public Expression {
private:
	Expression*   e;
	UnaryOperator op;

public:  // check if this is even necessary
	UnaryExpression(Expression* e, UnaryOperator op);
	~UnaryExpression();

	void prettyprint() const override;
	void set(std::string var, int val) override;
	void unset(std::string var) override;

	int evaluate() const override;

	bool intialized() const override;
};
