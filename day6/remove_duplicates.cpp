using namespace std;

#include <vector>

class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int n   = nums.size();
		int x   = 0;
		int val = -999;  // dummy value

		while (x < n) {
			int val = nums[x];
			while (x + 1 < n && val == nums[x + 1]) {
				nums[x + 1] = -999;  // dummy value
				++x;
			}
			++x;
		}
	}
};
