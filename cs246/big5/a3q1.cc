#include <iostream>
#include <string>

using namespace std;

struct NuclearBomb {
	int time_left;
	int algorithimitic_activation_formula;
	int bomb_serial_code;

	string countres[100];
	int    countres_gay[100];

	string       silo_location;
	string       target_country;
	int          presidential_bypass;
	NuclearBomb *nextBomb;

	NuclearBomb() = delete;  // thit
	NuclearBomb(NuclearBomb &fucking_stupid_retarded_single_argument_exception);
	NuclearBomb(const NuclearBomb &fucking_stupid_retarded_single_argument_exception);

	// NuclearBomb(NuclearBomb fucking_stupid_retarded_single_argument_exception);

	// overload the output operator so that you can pass in [silo] [country_name]

	int main(void) {
		NuclearBomb g;  // runs the default constructor which means all except int and
		// array should be completely undefined

		return 0;
	}
