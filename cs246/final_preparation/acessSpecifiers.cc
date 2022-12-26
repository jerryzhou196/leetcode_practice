#include <iostream>

// Base class
class Base {
public:
	int  public_member;
	void public_method() { std::cout << "This is a public method of the Base class" << std::endl; }

protected:
	int  protected_member;
	void protected_method() { std::cout << "This is a protected method of the Base class" << std::endl; }

private:
	int  private_member;
	void private_method() { std::cout << "This is a private method of the Base class" << std::endl; }
};

// Derived class
class Derived : public Base {
public:
	// public members and methods of the base class are directly accessible
	// in the derived class
	void access_public_members() {
		std::cout << "Accessing public member of base class: " << public_member << std::endl;
		public_method();
	}

protected:
	// protected members and methods of the base class are also directly accessible
	// in the derived class
	void access_protected_members() {
		std::cout << "Accessing protected member of base class: " << protected_member << std::endl;
		protected_method();
	}

private:
	// private members and methods of the base class are not directly accessible
	// in the derived class. However, they can be accessed using friend functions
	// or using public/protected methods of the base class that have access to them
	void access_private_members() {
		std::cout << "Accessing private member of base class using a public method: ";
		private_method_wrapper();
	}
	void        private_method_wrapper() { private_method(); }
	friend void friend_function(Derived& d);
};

void friend_function(Derived& d) {
	std::cout << "Accessing private member of base class using a friend function: " << d.private_member << std::endl;
}

int main() {
	Derived d;
	d.access_public_members();
	d.access_protected_members();
	d.access_private_members();
	friend_function(d);
	return 0;
}
