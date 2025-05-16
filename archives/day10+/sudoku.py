from collections import defaultdict

from typing import *

# [
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
#   [3, 3, 4, 5, 6, 6, 5, 6, 6],
# ]

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(1) = O(29159295120582489012518290581902850129501)
        for l in board:
            # len(l) == 9
            if len(set(l)) != 9:
                return False

        for i in range(9):
            seen = set()
            for j in range(9):
                seen.add(board[j][i])
            if len(seen) != 9:
                return False

        for i in range(3):
            for j in range(3):
                seen = set()
                seen.add(board[i * 3][j * 3])
                seen.add(board[i * 3 + 1][j * 3])
                seen.add(board[i * 3 + 2][j * 3])
                seen.add(board[i * 3][j * 3 + 1])
                seen.add(board[i * 3 + 1][j * 3 + 1])
                seen.add(board[i * 3 + 2][j * 3 + 1])
                seen.add(board[i * 3][j * 3 + 2])
                seen.add(board[i * 3 + 1][j * 3 + 2])
                seen.add(board[i * 3 + 2][j * 3 + 2])
                if len(seen) != 9:
                    return False

        return True


sln = Solution()
print(sln.isValidSudoku(board))
