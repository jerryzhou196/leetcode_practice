class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in d:
                stack.append(d[char])
            elif len(stack) > 0 and char != stack.pop():
                return False
            else:
                return False
        return len(stack) == 0
