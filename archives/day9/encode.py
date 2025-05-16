class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        ans = ""
        for string in strs:
            ans = ans + str(len(string)) + "#" + string
        return ans

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        index = 0
        ans = []
        while index < len(str):
            if int(str[index]):
                start = index
                while str[index] != "#":
                    index += 1
                iterations = int(str[start:index])
                index += 1
                ans.append(str[index : index + iterations])
                index += iterations
            else:
                index += 1
        return ans


s = Solution()

input = ["lint", "code", "love", "you"]
print(s.decode(s.encode(input)))
# Output: ["lint", "code", "love", "you"]
