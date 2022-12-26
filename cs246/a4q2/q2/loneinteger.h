#include <string>
#include "expression.h"

class LoneInteger : public Expression {
private:
	int val;

public:  // check if this is even necessary
	LoneInteger(int val);
	std::string prettyprint() const override;
	void        set(std::string var, int val) override;
	void        unset(std::string var) override;
	int         evaluate() const override;
	bool        intialized() const override;
	Expression* get_copy() const override;
};
