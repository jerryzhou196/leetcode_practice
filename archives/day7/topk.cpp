using namespace std;

#include <map>
#include <vector>

class Solution {
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		map<int, int> total;

		int n = nums.size();

		for (int x = 0; x < n; ++x) {
			auto it = total.find(nums[x]);
			if (it != total.end()) {
				nums[x]++;
			} else {
				nums[x] = 1;
			}
		}
	}

	void swap(int idx1, int idx2, vector<int>& nums) {
		int temp   = nums[idx1];
		nums[idx1] = nums[idx2];
		nums[idx2] = temp;
	}

	int partition(vector<int>& nums, map<int, int>& weight, int start, int end) {
		int pivot = end;
		for (int x = start; x < end; ++x) {
			if (weight[nums[x]] > weight[nums[pivot]]) {
				swap(x, pivot, nums);
			}
		}
	}

	void sortByWeight(vector<int>& nums, map<int, int>& weight, int start, int end) {
		int p = partition(nums, weight, start, end);
		sortByWeight(nums, weight, start, p);
		sortByWeight(nums, weight, p + 1, end);
	}
};
