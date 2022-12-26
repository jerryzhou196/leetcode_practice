class Province;

class City {
	void accept(Alberta& p) {}
	void accept(Ontario& p);
	void accept(Vancouver& p);
};

class Province {
	virtual void visit(City& c) = 0;
};

class Alberta : public Province {
	void visit(City& c) override { return c.accept(*this); }
};

class Vancouver : public Province {
	void visit(City& c) override { return c.accept(*this); }
};

class Ontario : public Province {
	void visit(City& c) override { return c.accept(*this); }
};

int main(void) {}
