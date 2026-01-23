class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left, right = i, j
            while left < right:
                print(left, right)
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        
        check(0, len(s) - 1)

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length - 1):
                    return s[start:start+length]
            
                
                
