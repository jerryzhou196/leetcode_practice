class Solution:
    def storeFirstOptions(self, s: str, startPos: int, firstOptions: list[str]) -> int:
        # If the current character is not '{', it is just one fixed character
        if s[startPos] != "{":
            firstOptions.append(s[startPos])
        else:
            # Collect all letters inside the braces
            while s[startPos] != "}":
                if "a" <= s[startPos] <= "z":
                    firstOptions.append(s[startPos])
                startPos += 1

            # Sort options alphabetically
            firstOptions.sort()

        # Return the next position after this character/group
        return startPos + 1

    def findAllWords(self, s: str, startPos: int) -> list[str]:
        # Base case: no characters left, so there is one empty suffix
        if startPos == len(s):
            return [""]

        firstOptions = []

        # Parse the next character/group of choices
        remStringStartPos = self.storeFirstOptions(s, startPos, firstOptions)

        # Recursively expand the rest of the string
        wordsWithRemString = self.findAllWords(s, remStringStartPos)

        expandedWords = []

        # Put each possible first character in front of each possible suffix
        for c in firstOptions:
            for word in wordsWithRemString:
                expandedWords.append(c + word)

        return expandedWords

    def expand(self, s: str) -> list[str]:
        return self.findAllWords(s, 0)


if __name__ == "__main__":
    sol = Solution()

    s = "{a,b}{d,e}"
    result = sol.expand(s)

    print(result)
