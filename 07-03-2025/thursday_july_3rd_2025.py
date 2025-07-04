class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix), len(matrix[0])
        def getVal(val):
            row = val // y
            col = val % y
            return matrix[row][col]

        left, right = 0, (x * y) - 1
        while left <= right:
            m = (left + right) // 2
            m_val = getVal(m)
            if m_val == target: return True
            if target < m_val: right = m - 1
            elif target > m_val: left = m + 1
        
        return False
