from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_map = {}
        occurences = {}
        for anagram in strs:
            occurences[anagram] = (
                occurences[anagram] + 1 if anagram in occurences else 1
            )

            for letter in anagram:
                if letter not in letter_map:
                    letter_map[letter] = [anagram]
                else:
                    letter_map[letter].append(anagram)

        ans = []
        remainder = []
        for anagram in strs:
            if len(anagram) > 0:
                starting_set = letter_map[anagram[0]]
                remainder = {associate: True for associate in starting_set}

                for index, letter in enumerate(anagram, 1):
                    associated_anagrams = letter_map[letter]
                    # for each remainder, see if they still exist in the current iteration
                    for key in list(remainder):
                        if key not in associated_anagrams or key not in occurences:
                            del remainder[key]

            elif anagram in occurences and occurences[anagram] > 0:
                remainder.append("")

            if len(remainder) > 0:
                for key in remainder:
                    ans.append(key)
                    if key in occurences and occurences[key] > 1:
                        occurences[key] -= 1
                    elif key in occurences:
                        del occurences[key]

        return ans


anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(anagrams))
