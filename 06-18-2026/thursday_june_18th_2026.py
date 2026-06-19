class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        @lru_cache(maxsize=100000)
        def dfs(i, j):
            # print(i, j, matrix[i][j])
            ans = 1 
            for y, x in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                yy, xx = i + y, j + x
                if yy >= 0 and yy < n and xx >= 0 and xx < m and matrix[yy][xx] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(yy, xx))
            return ans
    
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        
        return ans 
