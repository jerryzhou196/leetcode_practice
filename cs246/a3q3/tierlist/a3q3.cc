#include "list.h"
#include "tierlist.h"
#include <cassert>
#include <iostream>
// output operators to test iteration.
std::ostream &operator<<(std::ostream &out, const TierList::value_type &entry) {
  out << "[tier " << entry.tier << "]: " << entry.entry;
  return out;
}

std::ostream &operator<<(std::ostream &out, const TierList &l) {
  out << l.size() << std::endl;

  for (auto s : l) {
    out << s << std::endl;
  }
  return out;
}

using namespace std;
//  test-harness operators
enum Op {
  NONE,
  CONSTRUCT,
  DELETE,
  COPY,
  MOVE,
  ASSIGN_COPY,
  ASSIGN_MOVE,
  READ,
  PRINT,
  POP_BACK_TIER,
  PUSH_BACK_TIER,
  PRINT_FIRST_TIER,
  POP_FRONT_AT_TIER
};

// converts a one-character input comment into its corresponding test-harness
// operator
Op convertOp(string opStr) {
  switch (opStr[0]) {
  case 'c':
    return CONSTRUCT;
  case 'C':
    return COPY;
  case 'M':
    return MOVE;
  case 'd':
    return DELETE;
  case 'a':
    return ASSIGN_COPY;
  case 'A':
    return ASSIGN_MOVE;
  case 'r':
    return READ;
  case 'D':
    return POP_FRONT_AT_TIER;
  case 'p':
    return PRINT;
  case 'b':
    return POP_BACK_TIER;
  case 'B':
    return PUSH_BACK_TIER;
  case 'F':
    return PRINT_FIRST_TIER;
  default:
    return NONE;
  } // switch
} // convertOp

// Clears the cin error flags if invalid input is READ. Discards any input to
// the end of the line.
void fixcin() {
  cin.clear();
  string discard;
  getline(cin, discard);
} // fixcin

// Reads a TierList id (m#) from cin.
// If the value read has a valid format (m#, where 0 <= m <= 9), the parameter
// is set to the number read. The return value indicates whether the read value
// has a valid format or not.
bool readName(int &index) {
  const string errmsg = "Invalid name of TierList variable.";
  char m;
  cin >> m;
  if (m != 'm') {
    fixcin();
    cerr << errmsg << endl;
    return false;
  } // if

  index = -1;
  cin >> index;
  if (index < 0 || index > 9) {
    fixcin();
    cerr << errmsg << endl;
    return false;
  } // if
  return true;
} // readName

// Returns true if the pointer is a nullptr as required.
bool pointerMustBeNull(TierList *ptr, int index) {
  if (ptr != nullptr) {
    cerr << "List m" << index << " is initialized and needs to be a nullptr."
         << endl;
    fixcin();
    return false;
  } // if
  return true;
} // pointerMustBeNull

// Returns true if the pointer is a nullptr as required.
bool pointerMustNotBeNull(TierList *ptr, int index) {
  if (ptr == nullptr) {
    cerr << "TierList m" << index
         << " is not initialized and needs to not be a nullptr." << endl;
    fixcin();
    return false;
  } // if
  return true;
} // pointerMustNotBeNull

// Reads in a TierList index as m#.
bool readListIndex(int &index, TierList *lists[]) {
  // Suppress warning on lists
  assert(lists);
  if (!readName(index))
    return false;
  return true;
} // readListIndex

// Given a TierList, inserts an element at the front of the given tier.
void readList(TierList **lists) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    size_t tier;
    cin >> tier;
    if (cin.fail()) {
      fixcin();
      cerr << "Tier must be an size_t." << endl;
      return;
    }

    if (tier >= lists[index]->tierSize()) {
      cerr << "Tier " << tier << " is out of range on"
           << "TierList m" << index << endl;
      return;
    }

    std::string value;
    cin >> value;
    if (cin.fail()) {
      fixcin();
      cerr << "List element must be an integer." << endl;
      return;
    }
    lists[index]->push_front_at_tier(tier, value);
  }
} // readList

// Removes the first element in a given tier in a tier list.
void popFrontAtTier(TierList **lists) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    size_t tier;
    cin >> tier;
    if (cin.fail()) {
      fixcin();
      cerr << "Tier must be an size_t." << endl;
      return;
    }

    if (tier >= lists[index]->tierSize()) {
      cerr << "Tier " << tier << " is out of range on"
           << "TierList m" << index << endl;
      return;
    }
    lists[index]->pop_front_at_tier(tier);
  }
} // readList

// Create a TierList using the constructor to set the dimensions, then read in
// the values from cin.
void buildList(TierList *lists[]) {
  int index;
  if (readName(index)) {
    lists[index] = new TierList();
  } // if
} // buildList

// Invoke the destructor on the TierList.
void deleteList(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    delete lists[index];
    lists[index] = nullptr;
    cout << "List m" << index << " deleted" << endl;
  } // if
} // deleteList

// Use operator<< to output the TierList.
void printList(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    cout << "TierList m" << index << " =\n" << *(lists[index]) << endl;
  } // if
} // printList

// Use TierList move constructor to move contents of one TierList to another,
// temporary TierList.
void moveList(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    TierList m(std::move(*lists[index]));
    cout << "New TierList =\n"
         << m << "\nm" << index << " =\n"
         << *(lists[index]) << endl;
  } // if
} // moveList

// Use TierList copy constructor to copy contents of one TierList to another,
// temporary TierList.
void copyList(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    TierList m(*lists[index]);
    cout << "New TierList =\n"
         << m << "\nm" << index << " =\n"
         << *(lists[index]) << endl;
  } // if
} // copyList

// Use TierList copy assignment operator to copy contents of one TierList to
// another.
void assignCopyList(TierList *lists[]) {
  int index1, index2;
  if (readListIndex(index1, lists) &&
      pointerMustNotBeNull(lists[index1], index1) &&
      readListIndex(index2, lists) &&
      pointerMustNotBeNull(lists[index2], index2)) {
    *lists[index1] = *lists[index2];
    cout << "New TierList =\n"
         << *(lists[index1]) << "\nold TierList =\n"
         << *(lists[index2]) << endl;
  } // if
} // assignCopyList

// Use TierList move assignment operator to move contents of one TierList to
// another.
void assignMoveList(TierList *lists[]) {
  int index1, index2;
  if (readListIndex(index1, lists) &&
      pointerMustNotBeNull(lists[index1], index1) &&
      readListIndex(index2, lists) &&
      pointerMustNotBeNull(lists[index2], index2)) {
    *lists[index1] = std::move(*lists[index2]);
    cout << "m" << index1 << " =\n"
         << *(lists[index1]) << "\nm" << index2 << " =\n"
         << *(lists[index2]) << endl;
  } // if
} // assignMoveList

// Use pop_back to remove the last tier of the TierList.
void popBackTier(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    lists[index]->pop_back_tier();
    cout << "TierList m" << index << " popped off tier" << endl;
  } // if
} // printList

// Use push_back to add a new tier to the TierList.
void pushBackTier(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    lists[index]->push_back_tier();
    cout << "TierList m" << index << " pushed new tier" << endl;
  } // if
} // printList

// Prints out the _first_ element in each tier.
void printFirstTier(TierList *lists[]) {
  int index;
  if (readListIndex(index, lists) &&
      pointerMustNotBeNull(lists[index], index)) {
    auto i = lists[index]->begin();
    while (i != lists[index]->end()) {
      cout << *i << endl;
      i = i >> 1;
    }
    i = i << 1;
    if (i == lists[index]->end())
      return;
    do {
      cout << *i << endl;
      if (i == lists[index]->begin())
        break;
      i = i << 1;
    } while (true);
  } // if
}
int main() {
  TierList *lists[10] = {nullptr};

  for (;;) {
    cerr << "Command: ";
    string command;
    cin >> command;

    if (cin.eof())
      break;

    Op op = convertOp(command);

    switch (op) {
    case CONSTRUCT:
      buildList(lists);
      break;
    case DELETE:
      deleteList(lists);
      break;
    case READ:
      readList(lists);
      break;
    case PRINT:
      printList(lists);
      break;
    case MOVE:
      moveList(lists);
      break;
    case COPY:
      copyList(lists);
      break;
    case ASSIGN_COPY:
      assignCopyList(lists);
      break;
    case ASSIGN_MOVE:
      assignMoveList(lists);
      break;
    case PUSH_BACK_TIER:
      pushBackTier(lists);
      break;
    case POP_BACK_TIER:
      popBackTier(lists);
      break;
    case PRINT_FIRST_TIER:
      printFirstTier(lists);
      break;
    case POP_FRONT_AT_TIER:
      popFrontAtTier(lists);
      break;
    default:
      cerr << "Invalid command." << endl;
      break;
    } // switch
  }   // for

  for (int i = 0; i < 10; i++)
    delete lists[i];
} // main
