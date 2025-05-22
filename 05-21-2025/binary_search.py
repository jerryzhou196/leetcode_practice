from typing import *


def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    ans = []
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return True
        elif target < nums[m]:
            right = m - 1
        elif target > nums[m]:
            left = m + 1

    return False


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 6.5))


# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, ^, 5, 6, 7, 8]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, ^, 5, 6, 7, 8]

# [1,2,5,6,7,9,10]
# [1, , , , , ,  ]

# [1, 2, 3]
# [0, 1, 2]

# 9 / 2 = 4.5 = 4

# [0, 1, 2]
# 0 + 2 = 2 / 2 = 1
