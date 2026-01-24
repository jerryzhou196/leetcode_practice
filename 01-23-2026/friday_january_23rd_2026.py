class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for _ in range(len(nums))]
        dp_min = [0 for _ in range(len(nums))]

        dp_max[0], dp_min[0] = nums[0], nums[0]
        res = nums[0]

        for i, num in enumerate(nums[1:]):
            dp_max[i + 1] = max(num * dp_max[i], dp_min[i] * num, num)
            dp_min[i + 1] = min(num * dp_max[i], dp_min[i] * num, num)
            res = max(res, dp_max[i + 1])

        print(dp_max, dp_min)
    
        return res
        



        # dp_max[i] = max(current * dp_max[i - 1], dp_min[i - 1] * current, current)
        # dp_min[i] = min(current * dp_max[i - 1], dp_min[i - 1] * current, current)
        
