class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for left, left_element in enumerate(nums[: len(nums) - 2]):
            if left > 0:
                if nums[left] == nums[left - 1]:
                    continue

            center = left + 1
            right = len(nums) - 1
            while center < right:
                temperature = nums[center] + nums[right] + nums[left]

                if temperature == 0:
                    ans.append([nums[center], nums[right], nums[left]])
                    center += 1
                    while center < len(nums) - 2 and nums[center] == nums[center - 1]:
                        center += 1

                if temperature < 0:
                    center += 1

                if temperature > 0:
                    right -= 1

        return ans
