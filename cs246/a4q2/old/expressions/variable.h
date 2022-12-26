#include <string>
#include "expression.h"

class Variable : public Expression {
private:
	std::string name;
	int         val;
	bool        initalized;

public:  // check if this is even necessary
	Variable(std::string name);
	void prettyprint() const override;
	void set(std::string var, int value) override;
	void unset(std::string var) override;
	int  evaluate() const override;

	bool intialized() const override;
};
