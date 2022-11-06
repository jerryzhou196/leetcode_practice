#include "gokart.h"
#include <ostream>
#include <string>

GoKart::GoKart(const std::string& driver)
    : driver{driver}, position(Position(0, 0)), velocity{0}, acceleration{0}, direction{N}, blueShellHits{0}, unitsStepped{0} {}

void GoKart::step() {
	velocity += acceleration;
	unitsStepped += velocity;
	switch (direction) {
		case N: position.ns += velocity; break;
		case S: position.ns -= velocity; break;
		case E: position.ew += velocity; break;
		case W: position.ew -= velocity; break;
	}
}

void GoKart::left() {
	switch (direction) {
		case N: direction = W; break;
		case S: direction = E; break;
		case E: direction = N; break;
		case W: direction = S; break;
	}
}

void GoKart::right() {
	switch (direction) {
		case N: direction = E; break;
		case S: direction = W; break;
		case E: direction = S; break;
		case W: direction = N; break;
	}
}

int GoKart::shellHits() const {
	return blueShellHits;
}

void GoKart::accelerate(int by) {
	acceleration = by;
}

Position GoKart::location() const {
	return position;
}

int GoKart::distance() const {
	return unitsStepped;
}

int GoKart::speed() const {
	return velocity;
}

int GoKart::acc() const {
	return acceleration;
}

Direction GoKart::facing() const {
	return direction;
}

std::string GoKart::driverName() const {
	return driver;
}

void GoKart::blueshell() {
	acceleration = 0;
	velocity     = 0;

	int r = unitsStepped % 4;

	switch (r) {
		case 0: direction = N;
		case 1: direction = E;
		case 2: direction = S;
		case 3: direction = W;
	}
}
