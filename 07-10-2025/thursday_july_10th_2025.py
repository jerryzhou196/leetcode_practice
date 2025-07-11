"""Auto-generated on Tuesday, July 08, 2025."""

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = -1, len(nums1) - 1
        target_size = (len(nums1) + len(nums2)) // 2
        while True:
            m = (left + right) // 2
            m2 = target_size - m - 2

            l1 = nums1[m] if m >= 0 else -float('inf')
            l2 = nums2[m2] if m2 >= 0 else -float('inf')
            r1 = nums1[m + 1] if m + 1 < len(nums1) else float('inf')
            r2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            if r2 < l1:
                right = m - 1
            elif r1 < l2:
                left = m + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 1: return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2

                        
s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1, nums2))