class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:  
                    queue.append((0, i, j))

                if grid[i][j] != 0:
                    count += 1

        max_depth = 0
        # print(count)

        while queue:
            time, y, x = queue.popleft()
            # print(time, y, x, grid)
            if grid[y][x] == 3:
                continue
            max_depth = max(max_depth, time)
            count -= 1
            grid[y][x] = 3
            for i, j in [[0,1], [1, 0], [-1, 0], [0, -1]]:
                if y + i < 0 or y + i >= n or x + j < 0 or x + j >= m or grid[y + i][x + j] != 1:
                    continue 
                queue.append((time + 1, y + i, x + j))
    
        # print(count)
        return max_depth if count == 0 else -
