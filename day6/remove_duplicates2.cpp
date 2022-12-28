using namespace std;

#include <vector>

class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int n = nums.size();
		int i = 0;
		int j = 0;
		int k = 0;
		while (i < n) {
			++k;
			int val = nums[i];
			while (i < n && nums[i] == val) ++i;
			if (i != n) {
				++j;
				nums[j] = nums[i];
			}
		}
		return k;
	}
};
