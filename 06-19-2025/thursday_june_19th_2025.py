class Solution:
    def trap(self, height):
        s = []
        n = len(height)
        ans = 0
        for i in range(n):
            while s and height[i] >= height[s[-1]]:
                mid = s.pop()
                if len(s) == 0: 
                    continue 
                ans += (min(height[i], height[s[-1]]) - height[mid]) * (i - s[-1] - 1)
            s.append(i)
        
        return ans

s = Solution()
print(s.trap([9,2,4,1,6]))

                

            





