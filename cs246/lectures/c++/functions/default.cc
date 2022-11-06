#include <iostream>
#include <fstream>
using namespace std;

void printSuiteFile(string name = "suite.txt") {
  ifstream file(name.c_str());
  for (string s; file >> s;) cout << s << endl;
}

int main() {
  printSuiteFile();
  cout << endl;
  printSuiteFile("suite2.txt");
}

