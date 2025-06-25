class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def gen(entry = "", stack = [], quota = n):
            if quota == 0 and not stack: 
                ans.append(entry)

            if quota > 0:
                stack.append('(')
                gen(entry + '(', stack, quota - 1)
                stack.pop()
            
            if stack and stack[-1] == '(': 
                stack.pop()
                gen(entry + ')', stack, quota)
                stack.append('(')

        gen()
        return ans
