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
