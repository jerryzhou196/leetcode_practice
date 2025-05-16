from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_map = {}
        seen = {}

        for anagram in strs:
            for letter in anagram:
                if letter not in letter_map:
                    letter_map[letter] = [anagram]
                else:
                    letter_map[letter].append(anagram)

        ans = []

        for anagram in strs:
            if len(anagram) > 0:
                starting_set = letter_map[anagram[0]]
                remainder = {associate: True for associate in starting_set}

                for index, letter in enumerate(anagram, 1):
                    associated_anagrams = letter_map[letter]
                    # for each remainder, see if they still exist in the current iteration
                    for key in list(remainder):
                        if key not in associated_anagrams or key in seen:
                            del remainder[key]
            else:
                ans.append([""])

            if len(remainder) > 0:
                ans.append([key for key in remainder])
                seen.update({key: True for key in remainder})
        return ans


anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(anagrams))
