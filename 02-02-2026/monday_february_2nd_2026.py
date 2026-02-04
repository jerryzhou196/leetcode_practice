def binarySearch(target, nums):
    left, right = 0, len(nums) - 1
    while left <= right: 
        m = (left + right) // 2
        print(left, right, m)
        if nums[m] < target: 
            left = m + 1
        else: 
            right = m - 1
    return left
            

nums = [1,2,4,5,6,7,10]

for num in nums:
    binarySearch(num, nums)
    



