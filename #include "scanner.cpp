#include <deque>
#include <iostream>
#include <pair>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include "scanner.h"

using namespace std;

unordered_map<int, vector<string>> rhs_rules;
unordered_map<int, vector<string>> lhs_rules;

unordered_map<pair<int, string>, int> transitions;
unordered_map<pair<int, string>, int> reductions;

deque<string> symStack;
deque<string> inputSymbols;

void processCFG() {
	string line, lhs, rhs;
	int    line_num = 0;
	try {
		while (getline(std::cin, line)) {
			if (line == ".CFG") continue;
			if (line == ".INPUT") break;

			istringstream iss(line);
			j             iss >> lhs;
			lhs_rules[line_num].push_back(lhs);

			while (iss >> rhs) {
				rhs_rules[line_num].push_back(rhs);
			}

			line_num++;
		}

	} catch (const std::exception &e) {
		std::cerr << "ERROR" << e.what() << '\n';
	}
}

void processInput() {
	string word, line;

	try {
		while (getline(std::cin, line)) {
			if (line == ".ACTIONS") break;
			istringstream iss(line);
			while (iss >> word) {
				inputSymbols.push_back(word);
			}
		}
	} catch (const std::exception &e) {
		std::cerr << "ERROR" << e.what() << '\n';
	}
}

void printStacks() {
	try {
		bool printed = false;
		for (deque<string>::iterator it = symStack.begin(); it != symStack.end(); ++it) {
			cout << *it << " ";
			printed = true;
		}

		if (!printed) {
			cout << ". ";
		} else {
			cout << ". ";
		}

		for (deque<string>::iterator it = inputSymbols.begin(); it != inputSymbols.end(); ++it) {
			cout << *it << " ";
		}

		cout << endl;

	} catch (const std::exception &e) {
		std::cerr << "ERROR" << e.what() << '\n';
	}
}

void processTransitions() {
	string line, from_state, symbol, to_state;
	try {
		while (getline(std::cin, line)) {
			if (line == ".REDUCTIONS") break;
			istringstream iss(line);
			line >> from_state >> symbol >> to_state;
			transitions[make_pair(from_state, symbol)] = to_state;
		}
	} catch (const std::exception &e) {
		std::cerr << "ERROR: Transitions Invalid" << e.what() << '\n';
	}
}

void processReductions() {
	string line, state_number, rule_number, lookahead;
	try {
		while (getline(std::cin, line)) {
			if (cin.fail()) break istringstream iss(line);
			line >> state_number >> rule_number >> lookahead;
			reductions[make_pair(state_number, lookahead)] = rule_number;
		}
	} catch (const std::exception &e) {
		std::cerr << "ERROR: Transitions Invalid" << e.what() << '\n';
	}
}

int main() {
	std::string line;

	processCFG();

	processInput();

	processTransitions();

	processReductions();

	int    current_state = 0;
	string lookahead     = inputSymbols.front();

	try {
		while (lookahead != "ACCEPT") {
			if (transitions.find())

				if (lhs == "print") {
					printStacks();
				} else if (lhs == "reduce") {
					int    param;
					string param_s;
					iss >> param_s;
					param = stoi(param_s);

					if (lhs_rules.find(param) != lhs_rules.end()) {
						vector<string> rhs = rhs_rules[param];
						if (rhs[0] != ".EMPTY") {
							for (vector<string>::iterator it = rhs.begin(); it != rhs.end(); ++it) {
								symStack.pop_back();
							}
						}
						symStack.push_back(lhs_rules[param][0]);
					} else {
						throw runtime_error("Rule not found");
					}
				} else if (lhs == "shift") {
					string token = inputSymbols.front();
					inputSymbols.pop_front();
					symStack.push_back(token);
				}
		}
	} catch (const std::exception &e) {
		std::cerr << "ERROR" << e.what() << '\n';
	}
}
