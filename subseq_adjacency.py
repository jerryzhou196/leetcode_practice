from typing import *


class Solution:
    def isValid(self, word1, word2):
        difference = 0
        if len(word1) != len(word2):
            return False

        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                difference += 1
            if difference > 1:
                return False
        return difference == 1

    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        dp = [1 for _ in range(len(words))]
        prev = [-1] * len(words)

        global_max, global_max_i = 0, 0

        for index in range(1, len(words)):
            local_max, local_max_i = 0, -1
            for j in range(0, index):
                if (
                    self.isValid(words[j], words[index])
                    and groups[j] != groups[index]
                    and dp[j] >= local_max
                ):
                    local_max = dp[j]
                    local_max_i = j

            dp[index] = local_max + 1
            if local_max_i >= 0:
                prev[index] = local_max_i
            if dp[index] >= global_max:
                global_max, global_max_i = dp[index], index

        ans = []
        while global_max_i != -1:
            ans.append(words[global_max_i])
            global_max_i = prev[global_max_i]

        ans.reverse()

        return ans


# ["cb","ab","aa","ac","bc"]
# output: ["cb","ab","bb",     "bc"]
#         ["cb","ab","aa","ac","bc"]

# ["cb", "dc", "ab", "aa", "ac", "bb", "ca", "bcc", "cdd", "aad", "bba", "bc", "ddb"] (vals)
# [0,     1,    2,    3,    4,    5,   6,     7,     8,     9,     10,    11,   12] (indices)
# [-1,   -1,    0,    2,    3,    2,   3,    -1,    -1,    -1,     -1,     4,   -1] (prev)
# [1,     1,    2,    3,    4,    3,   4,     1,     1,     1,      1,     5,    1] (dp)

s = Solution()
print(
    s.getWordsInLongestSubsequence(
        [
            "cb",
            "dc",
            "ab",
            "aa",
            "ac",
            "bb",
            "ca",
            "bcc",
            "cdd",
            "aad",
            "bba",
            "bc",
            "ddb",
        ],
        [12, 6, 10, 11, 4, 8, 9, 11, 2, 11, 3, 2, 5],
    )
)

# ['cb','ab','aa','ac','bc']
# ['cb', 'ab', 'bb', 'bc']
