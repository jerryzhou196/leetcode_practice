class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> seen;
    int n = strs.size();
    for (int x = 0; x < n; ++x) {
      string copy = strs[x];
      sort(copy.begin(), copy.end());
      seen[copy].push_back(strs[x]);
    }

    vector<vector<string>> ans;

    for (auto i : seen) {
      ans.push_back((i).second);
    }

    return ans;
  }
};

int main(void) {}
