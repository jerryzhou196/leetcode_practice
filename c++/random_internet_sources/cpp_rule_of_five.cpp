

class rule_of_three {
  rule_of_three &operator=(const rule_of_three &other) { // III. copy assignment
    cstring = other.string;
  }
}
