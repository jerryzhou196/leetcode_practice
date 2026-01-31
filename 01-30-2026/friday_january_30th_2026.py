from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(str1, str2): 
            prefix = str1
            while str2.find(prefix) != 0: 
                prefix = prefix[:len(prefix) - 1]
                if prefix == "": return ""
            return prefix
    
        def divideAndConquer(start, end): 
            print(start, end)
            if start == end: return strs[start]
            m = (start + end) // 2
            lcp1 = divideAndConquer(start, m)
            lcp2 = divideAndConquer(m + 1, end) 
            return lcp(lcp1, lcp2)

        return divideAndConquer(0, len(strs) - 1)

         
        