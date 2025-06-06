class Solution:
    def c2(self, n):
        if n <= 0: return 1
        return (n) * (n - 1) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        barsAndStars = self.c2(n + 2)
        for i in range(3):
            barsAndStars -= self.c2(n + 2 - (limit + 1))
        return barsAndStars

s = Solution()
s.distributeCandies(1, 3)