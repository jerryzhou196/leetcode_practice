"""Auto-generated on Tuesday, July 08, 2025."""

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1) 
        target_size = (len(nums1) + len(nums2) - 1) // 2 
        while left <= right:
            m = (left + right) // 2
            right2 = (target_size - m) + 1
            if right2 < len(nums2) and nums2[right2] < nums1[m - 1]:
                right = m - 1
            elif m < len(nums1) and nums1[m] <= nums2[right2 - 1]:
                left = m + 1
            else:
                if len(nums1) + len(nums2) % 2 == 0:
                    return nums1[right - 1] 
                
        return 0.0
                        
s = Solution()
nums1 = [1,3]
nums2 = [3,4]
s.findMedianSortedArrays(nums1, nums2)