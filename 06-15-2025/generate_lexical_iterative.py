from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        curr_num = 1
        ans = []

        for _ in range(n):
            ans.append(curr_num)
            if curr_num * 10 <= n:
                curr_num *= 10
            else:
                if curr_num % 10 == 9:
                    curr_num /= 10
                curr_num += 1
        return ans

s = Solution()
print(s.lexicalOrder(113))