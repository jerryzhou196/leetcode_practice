from typing import *

class Solution:
    def zeroOutColumn(self, matrix, j):
        m, n = len(matrix), len(matrix[0])
        for i in range(m): 
            matrix[i][j] = 0

    def zeroOutRow(self, matrix, i):
        m, n = len(matrix), len(matrix[0])
        for j in range(m): 
            matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m): 
            for j in range(n):
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(m): 
            for j in range(n):
                if matrix[i][j] == 0 and (i == 0 or j == 0): 
                    self.zeroOutColumn(matrix, i)
                    self.zeroOutColumn(matrix, j)

        return matrix

s = Solution()
s.setZeroes(
    [[0,1,2,0],[3,0,0,2],[1,3,1,5]]
)


        

            
        