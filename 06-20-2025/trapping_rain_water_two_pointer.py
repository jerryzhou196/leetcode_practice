class Solution:
    def trap(self, height):
        n = len(height)
        left_max, right_max = 0, 0
        left, right = 0, n - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans += max(0, left_max - height[left])
                left_max = max(height[left], left_max)
                left += 1
            elif height[left] >= height[right]:
                ans += max(0, right_max - height[right])
                right_max = max(height[right], right_max)
                right -= 1
        return ans

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
            


