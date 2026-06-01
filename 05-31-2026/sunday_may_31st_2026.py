class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_cost = grid[n - 1][m - 1]
        
        costs = {}
        heap = []
        heappush(heap, [grid[0][0], (0, 0)])
        
        while heap: 
            e, point = heappop(heap)
            max_cost = max(max_cost, e)
            y, x = point
            
            grid[y][x] = 'X'
            
            if y == n - 1 and x == m - 1: 
                break 
            
            for i, j in [[0, 1], [1, 0], [-1 ,0], [0, -1]]: 
                yy, xx = y + i, x + j
                if yy < 0 or yy >= n or xx < 0 or xx >= m or grid[yy][xx] == 'X' :
                    continue 
                if (yy, xx) in costs: 
                    costs[(yy, xx)] = min(costs[(yy, xx)], grid[yy][xx])
                else: 
                    costs[(yy, xx)] = grid[yy][xx]

                heappush(heap, [grid[yy][xx], (yy, xx)])
        
        return max_cost

       
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        parent = list(range(n * m))
        rank = [0] * n * m
        def find(y):
            if parent[y] != y:
                parent[y] = find(parent[y])
            return parent[y]
        
        def union(x, y): 
            a, b = find(x), find(y)
            if find(x) != find(y):
                if rank[a] >= rank[b]: 
                    parent[b] = a 
                else: 
                    parent[a] = b
                if rank[a] == rank[b]: 
                    rank[a] += 1
        
        queue = deque([[n - 1, m - 1]])
        seen = set()
        edges = sorted([(y, x) for x in range(m) for y in range(n)], key=lambda x: grid[x[0]][x[1]])
        cost = 0
        
        for i , j in edges: 
            seen.add(i * n + j)
            for yy, xx in [[i, j + 1], [i + 1, j], [i - 1, j], [i, j - 1]]: 
                if yy < 0 or yy >= n or xx < 0 or xx >= m or not yy * n + xx in seen: 
                    continue 
                union(yy * n + xx, i * n + j)

            if find(0) == find((n - 1) * n + m - 1):
                return grid[i][j]
           
