#ifndef TIERLIST_H
#define TIERLIST_H

#include <string>
#include "list.h"
#include "tierlist.h"

class List;

class TierList {
private:
	// A tier list is a collection of lists.  Due to the
	// restrictions on time complexity for operations
	// on a tier list, a tier list is to be implemented
	// as an array of pointers to lists.
	List **tiers;

	size_t n;
	size_t capacity;

	void swap(TierList &other);

public:
	// Default constructor and destructor for a TierList.
	// The default constructor should initalize an empty tier list.
	TierList();
	~TierList();

	// Copy and move constructors for TierLists.
	// Copy should run in linear time in the number of elements in the tier list,
	// whilst move needs to run in constant time.
	TierList(TierList &&other);
	TierList(const TierList &other);

	// Copy and move assignment operators for TierLists.
	// Copy should run in linear time in the number of elements in the tier list,
	// whilst move needs to run in constant time.
	TierList &operator=(const TierList &other);
	TierList &operator=(TierList &&other);

	// Adds/removes a tier at the end of the tier list.
	// Tiers are indexed starting at 0.  Runs in time
	// at most _linear in the number of tiers_, but _not_ in the number
	// of elements.
	void push_back_tier();
	void pop_back_tier();

	// Adds/removes an element at the front of the given tier.
	// Must run in constant time.
	void push_front_at_tier(size_t tier, const std::string &entry);
	void pop_front_at_tier(size_t tier);
	// Returns the number of tiers.  Runs in constant time.
	size_t tierSize() const;
	// Returns the number of elements.  Can run in time
	// up to linear in the number of tiers.
	size_t size() const;

public:
	struct value_type {
		size_t      tier;
		std::string entry;
	};
	class iterator {
	private:
		friend class TierList;
		List **itiers;

		size_t curr_tier;

		List::iterator curr_item;

		const size_t &n;

		// this is possible with the power of friendship
		iterator(const size_t &n, List::iterator curr_item, List **p = nullptr, size_t curr_tier = -1);

	public:
		// Returns a value_type instance, holding on to
		// - a) the item the iterator points to
		// - b) the tier the item that the iterator points to lives at.
		value_type operator*() const;

		iterator &operator++();

		// New iterator operators which return a iterator pointing to the
		// start of the tier bk elements behind/fwd elements later
		// of the tier the iterator is currently on.
		//
		// If said tier is empty, the iterator moves back/forward to the next such
		// non-empty tier.
		iterator operator<<(int bk) const;
		iterator operator>>(int fwd) const;

		bool operator!=(const iterator &other) const;
		bool operator==(const iterator &other) const;
	};

	iterator begin() const;
	iterator end() const;
};

#endif
