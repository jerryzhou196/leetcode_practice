from typing import *
from collections import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seen = {}

        while j < len(s):
            if s[j] in seen:
                i = seen[s[j]]
            
            ans = max(ans, j - i + 1)
            seen[s[j]] = j + 1
            j += 1
        
        return ans





