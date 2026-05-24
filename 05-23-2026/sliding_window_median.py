from heapq import heappush, heappop
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left, right = [], []

        for i in range(k):
            heappush(left, -nums[i])
        for i in range(k // 2):
            heappush(right, -heappop(left))
        
        ans = []
        seen = defaultdict(int) 
        i = k - 1
        while True: 
            ans.append(-left[0] if k % 2 == 1 else (left[0] + right[0]) / 2)
            i += 1
            if k == len(nums): return ans

        
            in_val, out_val = nums[i], nums[i - k]
            seen[out_val] += 1
            
            if in_val <= -left[0]:
                heappush(left, -in_val)
                balance = -1
            else:
                balance = 1

            if out_val <= -left[0]: 
                balance += 1
            else: 
                balance -= 1
            
            print(left, right, seen, balance)
            
            while balance < 0: 
                heappush(left, -heappop(right))
                balance += 1
            
            while balance > 0: 
                heappush(right, -heappop(left))
                balance -= 1
            
            while left and seen[-left[0]] > 0:
                val = -heappop(left)
                seen[val] -= 1

            while right and seen[right[0]] > 0:
                val = heappop(right)
                seen[val] -= 1

if __name__ == "__main__":
    s = Solution()
    assert s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    print("All tests passed")
