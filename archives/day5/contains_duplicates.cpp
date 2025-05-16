class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    unordered_map<int, bool> map;
    int n = nums.size();
    for (int x = 0; x < n; ++x) {
      auto it = map.find(nums[x]);
      if (it == map.end()) {
        map[nums[x]] = true;
      } else {
        return true;
      }
    }
    return false;
  }
};

int main(void) {}
