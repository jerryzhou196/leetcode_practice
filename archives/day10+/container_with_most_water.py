class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                weaker_link = left
                while left < len(height) and height[left] <= height[weaker_link]:
                    left += 1
            else:
                weaker_link = right
                while right >= 0 and height[right] <= height[weaker_link]:
                    right -= 1

        return area
