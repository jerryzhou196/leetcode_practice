from typing import *

class Solution:
    def zeroMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        def zeroColumn(matrix, j): 
            for i in range(m): 
                matrix[i][j] =  '0'

        def zeroRow(matrix, i): 
            for j in range(n): 
                matrix[i][j] =  '0'


        for y in range(m): 
            for x in range(n): 
                if matrix[y][x] == '0': 
                    matrix[0][x] = '0'
                    matrix[y][0] = '0'

        for y in range(m): 
            for x in range(n): 
                if matrix[y][x] == '0': 
                    zeroRow(matrix, y)
                    zeroRow(matrix, x)

        return matrix
                    
s = Solution()
matrix = [
    ["0", "1", "0"],
    []
]
s.zeroMatrix()
                

            
                    
                




