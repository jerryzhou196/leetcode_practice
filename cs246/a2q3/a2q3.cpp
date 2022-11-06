#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using std::cerr;
using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::istream;
using std::istringstream;
using std::string;

void printBoard(char (&board)[3][3]) {
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			cout << "|";
			if (board[x][y] == 'o' || board[x][y] == 'x') {
				cout << board[x][y];
			} else {
				cout << " ";
			}
		}
		cout << "|" << endl;
	}
}

char hasVictory(char (&board)[3][3]) {
	// handle the vertical and horizontal victories

	for (int rc = 0; rc < 3; rc++) {  // rc = row or column

		int j_c = 0;  // this iterates down columns
		int j_r = 0;  // this iterates down rows

		while (j_c + 1 < 3 && board[rc][j_c] == board[rc][j_c + 1]) {
			++j_c;
		}

		while (j_r + 1 < 3 && board[j_r][rc] == board[j_r + 1][rc]) {
			++j_r;
		}

		if ((j_c == 2 && board[rc][j_c] == 'x') || (j_r == 2 && board[j_r][rc] == 'x')) {
			cout << "x won!" << endl;
			return 'x';
		} else if ((j_c == 2 && board[rc][j_c] == 'o') || (j_r == 2 && board[j_r][rc] == 'o')) {
			cout << "o won!" << endl;
			return 'o';
		}
	}

	// handle the cross victories
	int x = 0;
	int y = 0;
	while (y + 1 < 3 && x + 1 < 3 && board[x][y] == board[x + 1][y + 1]) {
		++x;
		++y;
	}

	if (x == y && x == 2 && board[x][y] == 'o') {
		cout << "o won!" << endl;
		return 'o';
	} else if (x == y && x == 2 && board[x][y] == 'x') {
		cout << "x won!" << endl;
		return 'x';
	}
	return '_';
}

void printSummary(int o_wins, int x_wins, int ties, int aborts) {
	cout << "x Wins:         " << x_wins << endl;
	cout << "o Wins:         " << o_wins << endl;
	cout << "Ties:           " << ties << endl;
	cout << "Aborted Games:  " << aborts << endl;
}

char processInput(istream &general_stream, char (&board)[3][3]) {
	// returns 'x', 'o', 'a' (abort), or 't' (tie)

	int  x      = -1;   // invalid default values
	int  y      = -1;   // invalid default values
	char player = '_';  // invalid default values

	int turn = 'x';

	char ans = '_';

	string raw_input;
	while (getline(general_stream, raw_input)) {
		istringstream input(raw_input);

		input >> player >> x >> y;

		int fail = input.fail();

		while (input.peek() == ' ') input.get();  // move char until non-empty space char

		if ((player == turn) && (x >= 0) && (x < 3) && (y >= 0) && (y < 3) && board[x][y] != 'x' && board[x][y] != 'y' && input.peek() == EOF &&
		    !fail) {  // check for ALL causes of an abort
			board[x][y] = player;

			turn = (turn == 'x') ? 'o' : x;

			printBoard(board);
			ans = hasVictory(board);
		} else {
			cerr << "Invalid move" << endl;
			ans = 'a';
			break;
		}
	}

	if (ans == '_') {  // this means no aborts were found but also no winner
		cerr << "Unfinished Game" << endl;
		ans = 't';
	}

	return ans;
}

void add_to(char a, int &x_wins, int &o_wins, int &aborts, int &ties) {
	switch (a) {
		case 'a': ++aborts; break;
		case 'x': ++x_wins; break;
		case 'o': ++o_wins; break;
		case 't': ++ties; break;
	}
}
int main(int argc, char *argv[]) {
	char board[3][3];
	int  unique = 0;

	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < 3; y++) {
			board[x][y] = unique;
			++unique;
		}
	}
	int error_occurred = 0;

	// x is row, y is column
	int  x      = -1;   // invalid default values
	int  y      = -1;   // invalid default values
	char player = '_';  // invalid default values
	char victory;

	int ties   = 0;
	int x_wins = 0;
	int o_wins = 0;
	int aborts = 0;

	if (argc == 1) {
		string raw_input;

		char result = processInput(cin, board);
		add_to(result, x_wins, o_wins, aborts, ties);

	} else {
		for (int args = 1; args < argc; args++) {
			ifstream game(argv[args]);

			if (game.fail()) {
				cerr << "Bad file" << endl;
				++aborts;
				continue;
			}

			char result = processInput(game, board);
			add_to(result, x_wins, o_wins, aborts, ties);

			unique = 0;
			for (int x = 0; x < 3; x++) {
				for (int y = 0; y < 3; y++) {
					board[x][y] = unique;
					++unique;
				}
			}
		}
	}
	printSummary(o_wins, x_wins, ties, aborts);
	return (aborts > 0) ? 1 : 0;
}
