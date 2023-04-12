from typing import List, Dict


class Solution(object):
    def analyzeSquare(self, threebythree):
        DEFAULT_ROW = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        seen = set()

        for row in threebythree:
            for item in row:
                if item in seen:
                    return False
                elif not item == ".":
                    seen.add(item)

        return DEFAULT_ROW - seen

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid_map: List[List[List[str]]] = [[None for _ in range(9)] for _ in range(9)]

        for square_y in range(0, 9, 3):
            for square_x in range(0, 9, 3):
                subsquare = [
                    row[square_x : square_x + 3]
                    for row in board[square_y : square_y + 3]
                ]
                subsquare_possiblities = self.analyzeSquare(subsquare)
                for y, row in enumerate(subsquare, start=square_y):
                    for x, item in enumerate(row, start=square_x):
                        if item == ".":
                            valid_map[y][x] = subsquare_possiblities

        # now we perform row check
        # we remove any values that have already been seen
        for y in range(9):
            for x in range(9):
                row_seen = [item for item in board[y] if not item == "."]
                column_seen = [item[x] for item in board if not item[x] == "."]

                if len(valid_map[y][x]) == 1:
                    row_seen.append()
                else:
                    valid_map[y][x] = [
                        item for item in valid_map[y][x] if item in row_seen
                    ]

                if len(valid_map[x][y]) == 1:
                    row_seen[valid_map[x][y][0]] = True
                else:
                    valid_map[x][y] = [
                        item for item in valid_map[x][y] if item in column_seen
                    ]

        for row in valid_map:
            for item in row:
                if item is not None and item == []:
                    return False
        return True


# Define a Sudoku board as a list of lists

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
solution = Solution()
result = solution.isValidSudoku(board)
print(result)
