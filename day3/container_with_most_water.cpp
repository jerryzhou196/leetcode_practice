#include <limits.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_x = INT_MIN, max_area = INT_MIN;
        int n = height.size();

        for (int x = 0; x < n; x++){
            
            if (height[x] > max_x){
                max_x = height[x]; 
                int max_y = height[n-1];
                max_area = max(max_area, calculateArea(max_y, height[x], n-1-x));

                for (int y = n - 2; y >= 0; y--){
                    if (height[y] > max_y){
                        max_y = height[y];
                        max_area = max(max_area, calculateArea(height[y], height[x], y-x));
                    }
                }
            }
        }
        
        return max_area;
    }

    int calculateArea(int h, int h2, int x){
        int height = min(h, h2);
        return height * x;
    }
};


int main(void){
    Solution s;
    vector<int> balls{1,8,6,2,5,4,8,3,7};
    cout << s.maxArea(balls);
    return 0;
}