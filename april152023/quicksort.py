import random


def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]

    pivot = random.choice(nums)

    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return nums[k]
    else:
        return quickselect(right, k - len(left) - len(middle))


# Test the function
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 4
print("The {}-th smallest number is {}".format(k, quickselect(nums, k)))
