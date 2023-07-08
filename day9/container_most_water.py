class Solution:
    def calculateArea(height, left, right):
        return height * (left - right)

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = 0
