from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans = 0, 0
        window_count = defaultdict(int)
        
        for r in range(len(s)):
            window_count[s[r]] += 1
            largest = max(window_count.items(), key=lambda x: x[1])[1]
            # print(f"largest: {largest}, r: {r}, l: {l}")
            if r - l + 1 - largest > k:
                window_count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans
