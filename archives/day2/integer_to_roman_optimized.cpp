#include <stdio.h>
#include <vector>
#include <string>
#include <map>
#include <iostream>

using namespace std;
// m = number of rows
// n = number of columns 

class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        map<int,string> letters{
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"},
        };
        for (auto x = letters.rbegin(); x != letters.rend(); x++){
            int n = num / x->first;
            if (n > 0){
                for (int i = 0; i < n; i++){
                    ans.append(x->second);
                    num -= (x->first);
                }
            }
        }
        return ans;
    }
};

int main(){
    Solution s;
    cout << s.intToRoman(1569);

    // printf("number of islands: %d", s.numIslands(vec));
    return 0;
}