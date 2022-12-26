class Vec2 {
	int x, y;

public:
	Vec2(int x, int y) : x{x}, y{y} {}
};

class Vec3 : public Vec2 {
	int z;

public:
	Vec3(int x, int y, int z)
	    : Vec2{x, y}, z{z} {}  // Vec2 doesn't have a default constructor, so you have to use the superclass constructor to initialize x and y
};

void f(Vec2* a) {  // takes in an array of 2D vector
	a[0] = Vec2{7, 8};
	a[1] = Vec2{9, 10};
}

int main() {
	Vec3 arr[2] = {{1, 2, 3}, {4, 5, 6}};
	f(arr);
}
