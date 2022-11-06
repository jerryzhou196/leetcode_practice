#include "tierlist.h"
#include <iostream>
#include <string>
#include <utility>
#include "list.h"

using namespace std;

TierList::TierList() : n{0}, capacity{0}, tiers{nullptr} {}

TierList::~TierList() {
	for (int x = 0; x < n; x++) {
		delete tiers[x];  // invokes the list.cc destructor
	}
}

void TierList::swap(TierList &other) {
	using std::swap;
	swap(n, other.n);
	swap(capacity, other.capacity);
	swap(tiers, other.tiers);
}

TierList::TierList(TierList &&other) : n{other.n}, capacity{other.capacity}, tiers{other.tiers} {}

TierList::TierList(const TierList &other) : n{other.n}, capacity{other.capacity} {
	for (int x = 0; x < n; x++) {
		tiers[x] = new List{*other.tiers[x]};  // invokes the list.cc copy constructor
	}
}

// whilst move needs to run in constant time.
TierList &TierList::operator=(const TierList &other) {
	TierList temp{other};
	swap(temp);
	return *this;
}
TierList &TierList::operator=(TierList &&other) {
	swap(other);
	return *this;
}

void TierList::push_back_tier() {
	if (n == capacity) {
		capacity *= 2;
		List **new_list = new List *[capacity];

		for (int x = 0; x < n; x++) {
			new_list[x] = tiers[x];
		}

		List **old = tiers;
		delete old;

		tiers = new_list;
	}
	tiers[n] = nullptr;
	++n;
}

void TierList::pop_back_tier() {
	if (n > 0) {
		delete tiers[n - 1];
		--n;
	}
}

void TierList::push_front_at_tier(size_t tier, const std::string &entry) {
	if (tier < n) {
		tiers[tier]->push_front(entry);
	}
}
void TierList::pop_front_at_tier(size_t tier) {
	if (tier > 0 && tier < n) {  // this check is not necessary as the test harness acounts for it
		delete tiers[tier];
	}
}

size_t TierList::tierSize() const {
	return n;
}

size_t TierList::size() const {
	return (*tiers)->size();
}

TierList::iterator TierList::end() const {
	iterator i(n, tiers[n - 1]->end(), nullptr, -1);  // change this to directly initialize nullptr
	return i;
}

TierList::iterator TierList::begin() const {    // the const keyword sets the this to be const *this
	iterator i(n, tiers[0]->begin(), this, 0);  // possible because of friendship
	return i;
}

//  --------------------------------------------------------------------------------
TierList::iterator::iterator(const size_t &n, List::iterator curr_item, const TierList *p, size_t curr_tier)
    : n{n}, curr_item{curr_item}, itiers{p}, curr_tier{curr_tier} {}

TierList::value_type TierList::iterator::operator*() const {
	value_type s;

	s.tier  = curr_tier;
	s.entry = *curr_item;

	return s;
}

//++ will take the iterator to the next item in a tier
TierList::iterator &TierList::iterator::operator++() {
	++curr_item;  // outsource

	if (curr_item == (itiers->tiers)[curr_tier]->end() && curr_tier < n) {
		while (curr_tier < n && !(itiers->tiers)[curr_tier]) ++curr_tier;  // take us to the nearest valid tier or n if there are none

		if (!(curr_tier < n)) {
			curr_item = (itiers->tiers)[curr_tier]->begin();
		}
	}

	return *this;
}

TierList::iterator TierList::iterator::operator<<(int bk) const {
	size_t sum = (int)curr_tier - bk;

	if (sum >= 0 && sum < curr_tier) {
		iterator i{n, (itiers->tiers)[sum]->begin(), itiers, sum};
		return i;
	} else {
		iterator i{n, (itiers->tiers)[sum]->end(), itiers};
		return i;
	}
}

TierList::iterator TierList::iterator::operator>>(int fwd) const {
	return *this << (-1 * fwd);
}

bool TierList::iterator::operator==(const iterator &other) const {
	return (curr_tier == other.curr_tier) && (curr_item == other.curr_item);  // outsource
}

bool TierList::iterator::operator!=(const iterator &other) const {
	return !(*this == other);
}

// REMINDER FOR Q2
// - remove unnecessary friendship
// - ensure you kept const properties
// - reimplement equal operator so that it is correct
// - change for loop to references if you use any for loop
// - include check for operator ++ that cur is even defined
