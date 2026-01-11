class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i in range(min(len(nums), k + 1)):
            if nums[i] in window: return True
            window.add(nums[i])

        for i in range(k + 1, len(nums)):
            window.remove(nums[i - k - 1])
            if nums[i] in window: return True
            window.add(nums[i])

        return False


        