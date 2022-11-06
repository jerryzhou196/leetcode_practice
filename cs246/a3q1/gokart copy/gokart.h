#ifndef GOKART_H
#define GOKART_H

#include <ostream>
#include <string>

struct Position {
	int ew, ns;
	Position(int ew = 0, int ns = 0) : ew{ew}, ns{ns} {}
};

enum Direction { N = 0, E, S, W };

class GoKart {
private:
	std::string driver;
	Position    position;
	int         velocity;
	int         acceleration;
	Direction   direction;
	int         blueShellHits;
	int         unitsStepped;

public:
	GoKart(const std::string& driver);
	void left();
	void right();
	void accelerate(int by);
	void blueshell();

public:
	int         distance() const;
	int         speed() const;
	int         acc() const;
	Direction   facing() const;
	int         shellHits() const;
	Position    location() const;
	std::string driverName() const;

public:
	void step();
};

#endif
