#include <iostream>
#include <string>

enum city { Pyongyang, Calgary, Toronto };

class Code {
	int  nuclear_code;
	int  activation_key;
	city city;
};

class Weapon {
	virtual void activate(int n) = 0;

	virtual Code* getCode() {
		city* nice = new city(Pyongyang);
		return nice;
	};
};

class Nuke : public Weapon {
}

class WeaponCreator {
	Weapon* getWeapon(char input) {
		switch (input) {
			case 'n': return Nuke();
		}
	}
};
