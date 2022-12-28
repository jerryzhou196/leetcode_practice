using namespace std;
#include <string>
#include <unordered_map>

class Solution {
public:
	int romanToInt(string s) {
		// NOTE: this problem is fundamentally flawed because it assumes s is a valid roman integer
		unordered_map<char, int> vals{
		    {'I', 1},
		    {'V', 5},
		    {'X', 10},
		    {'L', 50},
		    {'C', 100},
		    {'D', 500},
		    {'M', 1000},
		};
		int sum = 0;
		int n   = s.size();
		for (int x = 0; x < n; ++x) {
			int prev = (x == 0) ? 0 : x - 1;
			if (vals[s[prev]] < vals[s[x]]) {
				sum -= vals[s[prev]];
				sum += vals[s[x]] - vals[s[prev]];
			} else {
				sum += vals[s[x]];
			}
		}
		return sum;
	}
};
