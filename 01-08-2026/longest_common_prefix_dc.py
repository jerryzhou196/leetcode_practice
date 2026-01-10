from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(p1, p2):
            prefix = p1
            while p2.find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == '':
                    return prefix
            return prefix

        def split(start, end):
            if start == end: return strs[start]
            m = (start + end) // 2
            p1, p2 = split(start, m), split(m + 1, end)
            return lcp(p1, p2)
        
        return split(0, len(strs) - 1)


