from typing import *
from collections import defaultdict

class Solution:
    def isPalindrome(self, str): 
        m = len(str) // 2
        for i in range(m):
            if str[i] != str[len(str) - i - 1]: 
                return False
        
        return True

    def reverseString(self,str): 
        ans = []
        for char in range(len(str) - 1,  -1, -1): 
            ans.append(str[char])
        return "".join(ans)

    def longestPalindrome(self, words: List[str]) -> int:
        want = defaultdict(int)
        ans = 0

        for word in words: 
            if word in want:
                ans += len(word) * 2
                if want[word] == 1: 
                    del want[word]
                else: 
                    want[word] -= 1
            else: 
                want[self.reverseString(word)] += 1 

        largest_single_palindrome = 0

        for key in want.keys(): 
            if self.isPalindrome(key): 
                largest_single_palindrome = max(largest_single_palindrome, len(key))

        ans += largest_single_palindrome 
        
        return ans

