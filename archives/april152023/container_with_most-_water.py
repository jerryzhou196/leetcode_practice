class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        for i in range(height):
            for j in range(i + 1, height):
                max_area = max(max_area, (j - i) * min(height[j], height[i]))
        return max_area


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

s.maxArea
