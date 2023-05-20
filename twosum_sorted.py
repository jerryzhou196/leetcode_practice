class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, 1 if len(numbers) > 0 else 0
        while (numbers[start] + numbers[end] != target):

