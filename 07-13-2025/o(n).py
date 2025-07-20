from typing import *
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def is_subset(s1_count, s2_count):
            for char in s1_count.keys():
                if not (char in s2_count and s1_count[char] == s2_count[char]): return False
            return True

        count = Counter(s1)
        window_size = len(s1)
        window_count = Counter(s2[0: window_size - 1])
        for r in range(window_size - 1, len(s2)):
            window_count[s2[r]] += 1 
            # print(f"window_count: {window_count}, count: {count}")
            if is_subset(window_count, count) and is_subset(count, window_count): return True
            window_count[s2[r - (window_size - 1)]] -= 1
            if window_count[s2[r - (window_size - 1)]] == 0: 
                del window_count[s2[r - (window_size - 1)]]
        
        return False








