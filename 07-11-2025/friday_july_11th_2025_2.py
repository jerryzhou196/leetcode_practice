from typing import *
from collections import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans = 0,0, 0
        seen = set()
        s_list = []
        for char in s:
            s_list.append(char)

        while right <= len(s):
            while s_list[right] in seen:
                seen.remove(left)
                left += 1
            else:
                ans = max(ans, right - left + 1)
        
        return ans