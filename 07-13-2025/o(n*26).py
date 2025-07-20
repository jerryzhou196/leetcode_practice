from typing import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window_size = len(s1)
        window_count = Counter(s2[0: window_size - 1])

        matches = 0
        for char in window_count:
            if window_count[char] == count[char]:
                matches += 1

        for r in range(window_size - 1, len(s2)):
            if (window_count[s2[r]] == count[s2[r]]):
                matches -= 1
            window_count[s2[r]] += 1
            if (window_count[s2[r]] == count[s2[r]]):
                matches += 1

            if matches == len(set(s2)): return True 

            l = r - window_size + 1

            if (window_count[s2[l]] == count[s2[l]]):
                matches -= 1
            window_count[s2[l]] += 1
            if (window_count[s2[l]] == count[s2[l]]):
                matches += 1
        
        return False