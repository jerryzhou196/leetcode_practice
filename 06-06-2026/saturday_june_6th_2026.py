class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def mapEdge(y, x): 
            if y < 0 or y >= n or x < 0 or x >= m or board[y][x] == 'K' or board[y][x] == 'X': 
                return 
            
            board[y][x] = 'K'

            for i, j in [[0,1], [1,0], [-1, 0], [0, -1]]:
                mapEdge(y + i, x + j)
        
        for j in range(m):
            mapEdge(0, j)
            mapEdge(n - 1, j)

        for i in range(n):
            mapEdge(i, 0)
            mapEdge(i, m - 1)
        
        # print(board)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'K':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        return
