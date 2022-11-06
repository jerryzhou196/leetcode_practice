#include <iostream>
#include <sstream>
using namespace std;
const int MAX_INT_SETS = 5;

struct IntSet {
  int *data;
  int size;
  int capacity;
};

void init(IntSet &i) {
  i.data = nullptr;
  i.size = 0;
  i.capacity = 0;
} // Initialize to be "empty" with following field values: {nullptr,0,0}

void destroy(IntSet &i) {
  if (!(i.data == nullptr))
    delete[] i.data; // use VALGRIND to check if this is even necessary
}; // Clean up the IntSet and free dynamically allocated memory.

void add(IntSet &i, int e) { // Add element to the set i
  for (int x = 0; x < i.size; x++) {
    if (i.data[x] == e) {
      return; // theres a duplicate. we don't need to worry about it now
    }
  }

  int inital_capacity = i.capacity;

  if (i.size == 0)
    i.capacity = 5;

  if (i.size == i.capacity)
    i.capacity = i.capacity * 2;

  ++i.size;

  if (inital_capacity != i.capacity) {
    int *heap_arr = new int[i.capacity];

    for (int x = 0; x < i.size - 1; x++) {
      heap_arr[x] = i.data[x]; // copy current data to new resized heap array
    }

    heap_arr[i.size - 1] = e;
    delete[] i.data; // confirm with VALGRIND that this is the right way

    i.data = heap_arr;
  } else {
    i.data[i.size - 1] = e;
  }
}

IntSet operator|(const IntSet &i1, const IntSet &i2) {
  IntSet ans;
  init(ans); // dereference ans and pass by reference

  int n1 = i1.size;
  int n2 = i2.size;

  for (int x = 0; x < n1; x++) {
    add(ans, i1.data[x]);
  }

  for (int x = 0; x < n2; x++) {
    add(ans, i2.data[x]);
  }

  return ans;
}
// Set union.

bool isSubset(const IntSet &i1,
              const IntSet &i2) { // true if i2 is a subset of i1
  for (int x = 0; x < i2.size;
       x++) { // for each element in i2, check if it exists in i1
    int search = i2.data[x];
    bool found = 0;
    for (int y = 0; y < i1.size; y++) {
      if (i1.data[y] == search)
        found = 1;
    }
    if (!found)
      return false;
  }
  return true;
  // True if i2 is a subset of i1.}
}

IntSet operator&(const IntSet &i1, const IntSet &i2) {
  IntSet ans;
  init(ans); // dereference ans and pass by reference

  int n1 = i1.size;
  int n2 = i2.size;

  int seen1[n1]; // this tells future iterations to ignore these index as we
                 // have already added them
  int seen2[n2];

  int ignore1_n = 0;
  int ignore2_n = 0;

  int min1, min2;

  for (int x = 0; x < n1; x++)
    seen1[x] = 0;
  for (int x = 0; x < n2; x++)
    seen2[x] = 0;

  while ((ignore1_n < n1) || (ignore2_n < n2)) {
    for (int x = 0; x < n1; x++) {
      min1 = 0;
      while (seen1[min1])
        ++min1;
      for (int y = 0; y < n1; y++) {
        if (!seen1[y] &&
            (i1.data[y] < i1.data[min1])) { // if the index is still allowed to
                                            // be used and it's less than min
          min1 = y;
        }
      }
    }
    for (int x = 0; x < n2; x++) {
      min2 = 0;
      while (seen1[min2])
        ++min2;
      for (int z = 0; z < n2; z++) {
        if (!seen2[z] && (i2.data[z] < i2.data[min2])) {
          min2 = z;
        }
      }
    }
    if (i2.data[min2] >= i1.data[min1]) {
      ++ignore1_n;
      seen1[min1] = 1;
    }
    if (i2.data[min2] <= i1.data[min1]) {
      ++ignore2_n;
      seen2[min2] = 1;
    }

    if (i2.data[min2] == i1.data[min1])
      add(ans, i1.data[min1]);
  }

  return ans;

}; // Set intersection.

bool operator==(const IntSet &i1, const IntSet &i2) {
  return (isSubset(i1, i2) && isSubset(i2, i1));
}

bool contains(const IntSet &i, int e) {
  for (int x = 0; x < i.size; x++) {
    if (i.data[x] == e)
      return true;
  }
  return false;
} // True if set i contains element e.

void remove(IntSet &i, int e) {
  int x = 0;
  while ((x < i.size - 1) && i.data[x] != e) {
    ++x;
  }
  for (int y = x; y < i.size; y++) {
    i.data[y] = i.data[y + 1];
  }
  --i.size;
} // Remove element e from the set i.

// Output operator for IntSet.
std::ostream &operator<<(std::ostream &out, const IntSet &is) {
  bool seen_index[is.size];
  for (int x = 0; x < is.size; x++)
    seen_index[x] = false;

  cout << "(";
  for (int x = 0; x < is.size; x++) {
    int min = 0;
    while (seen_index[min])
      ++min;
    for (int y = 0; y < is.size; y++) {
      if (!seen_index[y] && is.data[min] <= is.data[y]) {
        min = y;
      }
    }
    cout << is.data[min] << ((x == is.size - 1) ? "" : ",");
    seen_index[min] = true;
  }
  cout << ")" << endl;

  return out;
}
// Input operator for IntSet. Continuously read int values from in and add to
// the passed IntSet. Function stops when input contains a non-int value.
// Discards the first non-int character.
std::istream &operator>>(std::istream &in, IntSet &is) {
  int num;
  while (in >> num) { // until we encounter EOF or a failure
    add(is, num);
  }

  return in;
}

// Test harness for IntSet functions. You may assume that all commands entered
// are valid. Valid commands: n <ind>,  p <ind>, & <ind1> <ind2>,
//                 | <ind1> <ind2>, = <ind1> <ind2>,
//                 s <ind1> <ind2>, c <ind1> <elem>,
//                 a <ind1> <elem>, r <ind1> <elem>,
//                 q/EOF
// SilentlyXR ignores invalid commands. Doesn't check that 0 <= index <
// MAX_INT_SETS. Do not test invalid commands!

int main(void) {
  // IntSet *ins = new IntSet();
  // init(*ins);
  // add(*ins, 5);
  // add(*ins, 5);
  // add(*ins, 6);
  // add(*ins, 7);

  IntSet ins1;
  init(ins1);
  cin >> ins1;
  cout << ins1;

  char next;
  cin >> next;

  while (!cin.eof()) {
    cout << next;
  }
  //   init(*ins1);
  //   add(*ins1, 4);
  //   add(*ins1, 5);
  //   add(*ins1, 6);

  //   IntSet *ins2 = new IntSet();
  //   init(*ins2);
  //   add(*ins2, 4);
  //   add(*ins2, 5);
  //   add(*ins2, 6);

  //   // bool nice  = (ins1 == ins);
  //   // bool copys = (ins1 == ins2);

  //   IntSet ballsack = (*ins1 | *ins2);
  //   cout << ballsack << endl;

  //   destroy(*ins1);
  //   destroy(*ins2);

  cout << "nice" << endl;
  return 0;
}
