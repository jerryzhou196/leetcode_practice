from typing import *

class Solution:
    def getHammingDistance(self, str1, str2): 
        differences = 0
        for i in range(max(len(str1), len(str2))): 
            c1, c2 = str1[i], str2[i] if i < len(str2) else False
            if c1 != c2:
                differences += 1
        return differences

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [False for _ in range(n)]
        prev = [-1 for _ in range(n)]
        local_max, local_max_index = 1, -1
        for i in range(n): 
            local_max, local_max_index = 1, -1
            for j in range(i, -1, -1): 
                if groups[i] != groups[j] and self.getHammingDistance(words[i], words[j]) == 1 and dp[j] + 1 > local_max: 
                    local_max, local_max_index = dp[j] + 1, j
                prev[i] = local_max_index
                dp[i] = local_max

        ans = []
        while local_max_index != -1: 
            ans.append(words[local_max_index])
            local_max_index = prev[local_max_index]

        return ans
             




def main() -> None:
    s = Solution()
    s.getWordsInLongestSubsequence(["ram", "dam", "bam", "ban", "gam"], [1, 1, 0, 2, 3])
    
    print("Hello from friday_may_16th_2025.py")

# input: 


# new ------------------------------------
# words = ["a", "c", "d", "e", "g"]
# indices = [1, 1, 0, 1, 0]

# f(i) = max(f(i), f(j) + 1)

# question to self: when could we use a recurrence that propagates the local_max through the previous_value...? 

# f(4) = max(

# ans = ["ram", "bam", "ban"]

if __name__ == "__main__":
    main()
