using namespace std;
#include <vector>

class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int insertIndex = 1;
		for (int i = 1; i < nums.size(); i++) {
			// We skip to next index if we see a duplicate element
			if (nums[i - 1] != nums[i]) {
				// Storing the unique element at insertIndex index and incrementing the insertIndex by 1
				nums[insertIndex] = nums[i];
				insertIndex++;
			}
		}
		return insertIndex;
	}
};

int main(void) {
	Solution    s;
	vector<int> ans{1, 2, 2, 3, 3, 4, 4, 4};
	s.removeDuplicates(ans);
}
