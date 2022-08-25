#include <limits.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution{
    public:
    int maxArea(vector<int> & height){
        int n = height.size();
        int l = 0, r = n - 1;
        int area = INT_MIN; 
        while (l < r){
            int h = min(height[l], height[r]);
            area = max(area, abs(r - l) * h);
            while (height[l] <= h && l < r) l++;
            while (height[r] <= h && l < r) r--;
        }
        return area;
    }
};

int main(){
    Solution s;
    vector<int> balls{1,8,6,2,5,4,8,3,7};
    cout << s.maxArea(balls);
    return 0;
}