#include <fstream>
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::ifstream;
using std::istream;
using std::strcmp;
using std::string;

struct wc_output {
  int lines;
  int words;
  int chars;
};

// implement hyphen algorithim
// can differ with whitesapce usage

wc_output compute_wc(istream &input, string name) {
  wc_output ans;
  int word_count = 0;
  int line_count = 0;
  int char_count = 0;

  if (input.good()) {
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
  }
  ans.chars = char_count;
  ans.lines = line_count;
  ans.words = word_count;

  cout << ans.lines << " " << ans.words << " " << ans.chars << name << endl;

  return ans;
}

int main(int argc, char *argv[]) {
  wc_output total;
  total.chars = 0;
  total.words = 0;
  total.lines = 0;

  bool hyped_detected;
  if (argc == 1) {
    total = compute_wc(std::cin, "");
  } else {
    for (int x = 1; x < argc; x++) {

      if (!strcmp(argv[x], "-")) {
        hyped_detected = true;
      } else {
        ifstream input(argv[x]);
        wc_output file = compute_wc(input, argv[x]);
        total.chars += file.chars;
        total.lines += file.lines;
        total.words += file.words;
      }
    }
  }

  if (hyped_detected) {
    wc_output hypen = compute_wc(std::cin, "-");
    total.chars += hypen.chars;
    total.lines += hypen.lines;
    total.words += hypen.words;
  }

  cout << total.lines << " " << total.words << " " << total.chars << " total"
       << endl;

  return 0;
}
