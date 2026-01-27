class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checkSquare(x,y):
            # check nums are 1 to 9
            required = set()
            for i in range(1, 10): 
                required.add(i)

            for i in range(x, x + 3): 
                for j in range(y, y + 3): 
                    if grid[i][j] in required: 
                        required.remove(grid[i][j])
                    else: 
                        return False 
                
            if len(required) != 0: return False
                
            # check diagonals
            left_to_right = 0
            for i in range(3): 
                left_to_right += grid[x + i][y + i]
        
            required_sum = left_to_right

            right_to_left = 0
            for i in range(3): 
                right_to_left += grid[x + 2 - i][y + i]
            
            # print(right_to_left)
            
            if right_to_left != required_sum: return False

            # check rows 
            for i in range(3): 
                row_sum = 0
                for j in range(3): 
                    row_sum += grid[x + i][y + j]
                if row_sum != required_sum: return False
        
            # check cols 
            for i in range(3): 
                col_sum = 0
                for j in range(3): 
                    col_sum += grid[x + j][y + i]
                if col_sum != required_sum: return False

            return True 
            
        
        # grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        ans = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                # print(i, j)
                if checkSquare(i, j):
                    ans += 1
        return ans
        





            
        