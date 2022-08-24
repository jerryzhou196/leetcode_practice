#include <stdio.h>
#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;
// m = number of rows
// n = number of columns 

class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        unordered_map<int,string> letters{
            {1, "I"},
            {5, "V"},
            {10, "X"},
            {50, "L"},
            {100, "C"},
            {500, "D"},
            {1000, "M"},
            {4, "IV"},
            {9, "IX"},
            {40, "XL"},
            {90, "XC"},
            {400, "CD"},
            {900, "CM"}
        };
        int thousand = num - (num % 1000); //equivalent to (num % 10000) - (num % 1000) since num <= 0
        int hundred = (num % 1000) - (num % 100);
        int ten = (num % 100) - (num % 10);
        int one = (num % 10); //equivalent to (num % 10) - (num % 1)

        addLetters(thousand, ans, letters);
        addLetters(hundred, ans, letters);
        addLetters(ten, ans, letters);
        addLetters(one, ans, letters);

        return ans;
    }
private: 
    void removeLargestMultiple(int &num, int fit, unordered_map<int, string> &letters, string &ans){
        int n = num / fit;
        num -= (n * fit);
        for (int x = 0; x < n; x++){
            ans.append(letters[fit]);
        }
    }

    void addLetters(int spaced, string &ans, unordered_map<int, string> &letters){
        unordered_map<int, string>::iterator search = letters.find(spaced);
        if (search != letters.end()){
            ans += letters[spaced];
        } else {
            removeLargestMultiple(spaced, 1000, letters, ans);
            removeLargestMultiple(spaced, 500, letters, ans);
            removeLargestMultiple(spaced, 100, letters, ans);
            removeLargestMultiple(spaced, 50, letters, ans);
            removeLargestMultiple(spaced, 10, letters, ans);
            removeLargestMultiple(spaced, 5, letters, ans);
            removeLargestMultiple(spaced, 1, letters, ans);
        }
    }
};

int main(){
    Solution s;
    cout << s.intToRoman(1569);

    // printf("number of islands: %d", s.numIslands(vec));
    return 0;
}