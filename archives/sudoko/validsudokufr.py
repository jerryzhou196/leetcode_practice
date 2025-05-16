from typing import List, Dict


class Solution(object):
    def isValidPosition(self, x, y, board):
        # check ro
        val = board[x][y]

        for item in range(0, 9):
            if y != item and board[x][item] == val:
                return False
            if x != item and board[item][y] == val:
                return False
        seen = {}

        for x in range((x // 3) * 3, (x // 3) * 3 + 3):
            for y in range((y // 3) * 3, (y // 3) * 3 + 3):
                if board[x][y] in seen:
                    return False
                elif board[x][y] != ".":
                    seen[board[x][y]] = True
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(0, 9):
            for col in range(0, 9):
                if not board[row][col] == "." and not self.isValidPosition(
                    row, col, board
                ):
                    return False
        return True


board = [
    ["7", ".", ".", ".", "4", ".", ".", ".", "."],
    [".", ".", ".", "8", "6", "5", ".", ".", "."],
    [".", "1", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "9", ".", ".", "."],
    [".", ".", ".", ".", "5", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]

s = Solution()
print(s.isValidSudoku(board))
