class Resource {
public:
	Resource(){};
	explicit Resource(const Resource& g) {}
};

void foo(Resource& r) {}

int main(void) {
	Resource r1;
	Resource r2(r1);

	foo(r1);

	// Resource r2 = r1: invalid
	// foo(r2): invalid

	return 0;
}
