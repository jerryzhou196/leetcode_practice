#include "list.h"
#include <iostream>
#include <string>
#include <utility>

using namespace std;

List::~List() {
	List::iterator a = begin();
	while (a != end()) {
		Node *tmp = a.cur;
		++a;
		delete tmp;
	}
}

List::List() : n{0}, head{nullptr} {}

List::iterator::iterator(List::Node *p) : cur{p} {}

List::iterator List::begin() const {
	iterator i(head);
	return i;
}
List::iterator List::end() const {
	iterator i{};
	return i;
}

List::iterator &List::iterator::operator++() {
	if (!cur) return *this;

	if (cur->next == nullptr) {
		cur = nullptr;
		return *this;
	}
	cur = cur->next;
	return *this;
}

const std::string &List::iterator::operator*() const {
	return (cur->value);
}

bool List::iterator::operator==(const iterator &other) const {
	if (other.cur && cur) {
		return ((other.cur)->value == (cur->value));
	} else if (!other.cur && !cur) {
		return true;
	}
	return false;
}

bool List::iterator::operator!=(const iterator &other) const {
	return !(other == *this);
}

void List::push_front(const std::string &value) {
	++n;

	Node *temp  = new Node();
	temp->value = value;
	temp->next  = head;

	head = temp;
}

List::List(List &&other) : n{other.n}, head{other.head} {
	other.n    = 0;
	other.head = nullptr;
}

List::List(const List &other) : n{other.n} {
	head = copy_node(other.head);
}

List::Node *List::copy_node(List::Node *other) {
	if (other) {
		Node *n  = new Node();
		n->value = other->value;
		n->next  = (other->next) ? copy_node(other->next) : nullptr;
		return n;
	} else {
		return nullptr;
	}
}

void List::swap(List &other) {
	using std::swap;
	swap(n, other.n);
	swap(head, other.head);
}

List &List::operator=(const List &other) {
	List temp{other};
	swap(temp);
	return *this;
}

List &List::operator=(List &&other) {
	swap(other);
	return *this;
}

void List::pop_front() {
	if (n > 0) {
		Node *temp = head;
		--n;
		head = head->next;
		delete temp;
	}
}

size_t List::size() const {
	return n;
}
