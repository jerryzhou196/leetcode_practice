#include <fstream>
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::ifstream;
using std::istream;
using std::string;

struct wc_output {
  int lines;
  int words;
  int chars;
};

wc_output compute_wc(istream &input) {
  wc_output ans;

  if (input.good()) {
    int word_count = 0;
    int line_count = 0;
    int char_count = 0;

    int is_seperator = 1;
    char c = input.get();
    while (c != EOF) {
      // cout << "char: " << c << endl;
      // cout << (c == '\n') << endl;

      if (c == ' ' || c == '\n') {
        is_seperator = 1;
      } else if (is_seperator) {
        ++word_count;
        is_seperator = 0;
      }

      if (c == '\n') {
        ++line_count;
      }
      ++char_count;
      c = input.get();
    }
    ans.chars = char_count;
    ans.lines = line_count;
    ans.words = word_count;
    return ans;
  }
}

int main(int argc, char *argv[]) {
  wc_output ans;
  if (argc == 1) {
    ans = compute_wc(std::cin);
    // continously takes in input in one buffer until EOF is reached
    // calculates stats for the total input
  } else {
    for (int x = 1; x < argc; x++) {
      ifstream input(argv[x]);
      ans = compute_wc(input);
    }
  }
  cout << "line count: " << ans.lines << endl;
  cout << "word count: " << ans.words << endl;
  cout << "char count: " << ans.chars << endl;
  return 0;
}
