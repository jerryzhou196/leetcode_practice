class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        return self.is_valid_string(0, 0, s, memo)

    def is_valid_string(self, index: int, open_count: int, s: str, memo: List[List[int]]) -> bool:
        # If reached end of the string, check if all brackets are balanced
        if index == len(s):
            return open_count == 0

        # If already computed, return memoized result
        if memo[index][open_count] != -1:
            return memo[index][open_count] == 1

        is_valid = False
        # If encountering '*', try all possibilities
        if s[index] == '*':
            is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo)  # Treat '*' as '('
            if open_count > 0:
                is_valid |= self.is_valid_string(index + 1, open_count - 1, s, memo)  # Treat '*' as ')'
            is_valid |= self.is_valid_string(index + 1, open_count, s, memo)  # Treat '*' as empty
        else:
            # Handle '(' and ')'
            if s[index] == '(':
                is_valid = self.is_valid_string(index + 1, open_count + 1, s, memo)  # Increment count for '('
            elif open_count > 0:
                is_valid = self.is_valid_string(index + 1, open_count - 1, s, memo)  # Decrement count for ')'

        # Memoize and return the result
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid


class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]

        # dp[i][j]: is substr starting from i possible with j open parenthesis 
        dp[n][0] = True 
        
        for i in range(n - 1, -1, -1): 
            for j in range(n, -1 ,-1):
                if s[i] == ')': 
                    if j > 0:
                        dp[i][j] = dp[i + 1][j - 1]
                elif s[i] == '(':
                    if j < n:
                        dp[i][j] = dp[i + 1][j + 1]
                else: 
                    dp[i][j] |= dp[i + 1][j + 1] if j < n else False
                    dp[i][j] |= dp[i + 1][j - 1] if j > 0 else False
                    dp[i][j] |= dp[i + 1][j] 

        return dp[0][0]


 class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        asterick_stack = []
        for i, c in enumerate(s):
            if c == '(':
                open_stack.append(i)
            elif c == '*': 
                asterick_stack.append(i)
            else: 
                if open_stack: 
                    open_stack.pop()
                elif asterick_stack: 
                    asterick_stack.pop()
                else:
                    return False
        
        for i in range(len(open_stack) - 1, -1 ,-1): 
            if asterick_stack and open_stack and asterick_stack[-1] > open_stack[-1]: 
                asterick_stack.pop()
                open_stack.pop()
            else:
                return False
            
        return len(open_stack) == 0 
        
        



