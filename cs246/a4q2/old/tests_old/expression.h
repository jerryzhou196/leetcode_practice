#include <string>
#ifdef __EXPRESSION_H__
#define __EXPRESSION_H__

class Expression {
public:
	virtual ~Expression(){};
	virtual void prettyprint() const           = 0;
	virtual void set(std::string var, int val) = 0;
	virtual void unset(std::string var)        = 0;
	virtual int  evaluate() const              = 0;
	virtual bool intialized() const            = 0;
};
#endif
