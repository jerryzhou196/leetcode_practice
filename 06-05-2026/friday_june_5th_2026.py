class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(x):
            if x == 1: return False
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0: return False
            return True

        if 8 <= n <= 11: return 11
        
        for i in range(1, 6):
            for j in range(10**(i - 1), 10**(i)):
                seed = str(j)
                rev = seed[::-1][1::]
                combined = int(seed + rev)
                if len(seed + rev) % 2 == 1 and combined >= n and isPrime(combined):
                    return combined 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        def dfs(y, x, prev_val, ocean):
            # print(y, x, prev_val, oceans[0], oceans[1])
            if y < 0 or y >= n or x < 0 or x >= m or ocean[y][x] or heights[y][x] < prev_val:
                return 
            ocean[y][x] = True 
            for i,j in [[0,1], [1,0], [-1, 0], [0, -1]]:
                dfs(y + i, x + j, heights[y][x], ocean)

        ans = []
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]
                
        for j in range(m):
            dfs(0,j, -float('inf'), pacific)
            dfs(n - 1, j, -float('inf'), atlantic)
            
        for i in range(n):
            dfs(i, 0, -float('inf'), pacific)
            dfs(i, m - 1, -float('inf'), atlantic)
    
        # print(pacific, atlantic)
        
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])


        return ans 

        
        
