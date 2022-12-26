#include "bettor.h"
#include "horserace.h"
#include "observer.h"
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
  string raceData = "race.txt";
  if (argc > 1) {
    raceData = argv[1];
  }

  HorseRace x{"nice"};
}
