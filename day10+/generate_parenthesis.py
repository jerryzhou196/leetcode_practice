class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(combination, l, r):
            if l < n:
                backtrack(combination + "(", l + 1, r)

            if r < l:
                backtrack(combination + ")", l, r + 1)

            if r >= l and l >= n:
                ans.append(combination)

        backtrack("(", 1, 0)

        return ans
