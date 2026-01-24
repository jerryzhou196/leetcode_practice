class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = defaultdict(bool)

        for word in wordDict:
            dictionary[word] = True

        ans = []

        # print(dictionary)

        def dfs(acc = [], index = 0, curr_string = ""):
            # print(acc, index, curr_string)
            if index == len(s):
                if curr_string in dictionary:
                    acc.append(curr_string)
                    ans.append(" ".join(acc))
                    acc.pop()
                return
            
            curr_string += s[index]

            dfs(acc, index + 1, curr_string)
            
            if curr_string in dictionary:
                acc.append(curr_string)
                dfs(acc, index + 1, "")
                acc.pop()

        dfs()
        return ans
