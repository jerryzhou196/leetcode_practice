
#include <string>
using namespace std;

class Enemy {
	string name;
	int    health;
	virtual ~Weapon()                   = 0;
	virtual void getStrikedBy(Weapon w) = 0;
};

class Weapon {
	string name;
	int    damage;

	virtual ~Weapon(){} = 0;

	virtual void strike(Enemy e) = 0;
};
