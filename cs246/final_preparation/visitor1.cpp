class Bullet;
class Turtle;
class Rock;
class Stick;
class Weapon;

class Enemy {
public:
	virtual void beStruckBy(Weapon& w) = 0;
};

class Weapon {
public:
	virtual void strike(Bullet& b) = 0;
	virtual void strike(Turtle& t) = 0;
};

class Bullet : public Enemy {
public:
	void beStruckBy(Weapon& w) override {
		w.strike(*this);  // this is a Bullet pointer
	}
};

class Turtle : public Enemy {
public:
	void beStruckBy(Weapon& w) override {
		w.strike(*this);  // this is a Turtle pointer
	}
};

class Rock : public Weapon {
public:
	void strike(Bullet& b) override {}
	void strike(Turtle& t) override {}
};

class Stick : public Weapon {
public:
	void strike(Bullet& b) override {}
	void strike(Turtle& t) override {}
};

int main() {
	Enemy*  e = new Turtle{};
	Weapon* w = new Rock{};
	e->beStruckBy(*w);
}
