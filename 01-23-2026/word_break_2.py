from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memoization = {}
        return self._dfs(s, word_set, memoization)

    # Depth-first search function to find all possible word break combinations
    def _dfs(
        self, remaining_str: str, word_set: set, memoization: dict
    ) -> List[str]:
        # Check if result for this substring is already memoized
        if remaining_str in memoization:
            return memoization[remaining_str]
        # Base case: when the string is empty, return a list containing an empty string
        if not remaining_str:
            return [""]
        results = []
        for i in range(1, len(remaining_str) + 1):
            current_word = remaining_str[:i]
            # If the current substring is a valid word
            if current_word in word_set:
                for next_word in self._dfs(
                    remaining_str[i:], word_set, memoization
                ):
                    # Append current word and next word with space in between if next word exists
                    results.append(
                        current_word + (" " if next_word else "") + next_word
                    )
        # Memoize the results for the current substring
        memoization[remaining_str] = results
        return results

s = Solution()
# s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
