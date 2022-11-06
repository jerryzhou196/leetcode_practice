#include <limits.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <cstdio>   

using namespace std; 

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        int nl = 0, nr = 0, m = 0;
        vector<vector<int>> ans; 
        unordered_map<int, vector<vector<int>>> map;

        if (n < 3){
            ans.push_back(nums);
            return ans;
        }

        sort(nums.begin(), nums.end());

        while (nums[m] < 0) m++;

        vector<int> L = split(nums, 0, m);
        vector<int> R = split(nums, m, n);

        insert(map, L, L.size());
        insert(map, R, R.size());

        for (int x = 0; x < n; x++){
            int search = 0 - nums[x]; 
            auto it = map.find(search);
            if (it != map.end()){
                for (auto e: map[search]){
                    e.push_back(nums[x]);
                    ans.push_back(e);
                }
            }
        }

        sort(ans.begin(), ans.end());
        ans.erase(unique(ans.begin(), ans.end()), ans.end());
        return ans;
    }

    private:
        vector<int> split(vector<int> &nums, int start, int end){
            int n = nums.size();
            vector<int> ret;
            for (int x = start; x < end; x++){
                ret.push_back(nums[x]);
            }
            return ret;
        }
        void insert(unordered_map<int, vector<vector<int>>> &map, vector<int> &split, int n){
            for (int x = 0; x < n; x++){
                for (int y = x + 1; y < n; y++){
                     auto find = map.find(sum);
                    if (find != map.end()){
                        vector<int> pair{split[y], split[x]};
                        map[sum].push_back(pair);
                    } else {    
                        vector<vector<int>> pair{{split[y], split[x]}};
                        map[sum] = pair; 
                    }
                }
            }

        }
};


int main(){
    Solution s;
    vector<int> balls{-1,0,1,0};
    // -4, -1, -1, 0, 1, 2
    vector<vector<int>> ugh = s.threeSum(balls);
    int n = ugh.size();
    return 0;
}