class Resource {
public:
  Resource() {
    // Allocate resources
  }
  ~Resource() {
    // Deallocate resources
  }
  Resource(const Resource &other) {
    // Copy resources from other
  }
  Resource &operator=(const Resource &other) {
    // Copy resources from other
    return *this;
  }
  Resource(Resource &&other) noexcept {
    // Move resources from other
  }
  Resource &operator=(Resource &&other) noexcept {
    // Move resources from other
    return *this;
  }
};

void foo(Resource r) {
  // Do something with r
}

int main() {
  Resource r1;
  Resource r2;

  // This will unintentionally copy r1 into foo()
  foo(r1);

  // This will unintentionally copy r1 into r2
  r2 = r1;

  return 0;
}
