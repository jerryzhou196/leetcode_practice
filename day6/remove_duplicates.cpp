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

		int new_index = 0;
		int k         = 0;

		for (int old_index = 0; old_index < n; old_index++) {
			if (nums[old_index] != -999) {
				++new_index;
				++k;
			}

			if (new_index != old_index && old_index != -999) {
				nums[new_index + 1] = nums[old_index];
				new_index           = old_index;
				++k;
			}
		}
		return k;
	}
};
