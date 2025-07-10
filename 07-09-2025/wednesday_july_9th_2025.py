"""Auto-generated on Tuesday, July 08, 2025."""

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1) - 1
        target_size = (len(nums1) + len(nums2)) // 2
        while left <= right:
            m = (left + right) // 2
            nums2_right = target_size - m 
            if nums2_right < len(nums2) and nums2[nums2_right] < nums1[0]:
                left = m + 1
            elif right < len(nums1) and nums1[right] < nums1[0]:
                right = m - 1
            else:
                a = nums1[right - 1] if right >= 1 else -float('inf')
                b = nums2[nums2_right - 1] if right >= 1 else -float('inf')
                
                if a > b:
                    return a if (len(nums1) + len(nums2)) % 2 == 1 else (nums1[right - 1] + nums1[right]) / 2
                else:
                    return b if (len(nums1) + len(nums2)) % 2 == 1 else (nums2[nums2_right - 1] + nums2[nums2_right]) / 2
        
        return 0.0

                        
s = Solution()
nums1 = [1,3]
nums2 = [3,4]
s.findMedianSortedArrays(nums1, nums2)