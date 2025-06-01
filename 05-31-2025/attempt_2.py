from dataclasses import dataclass
from collections import deque
from typing import *


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [0] * (n**2 + 1)
        val = 1
        for i in range(n - 1, -1, -1):
            if i % 2 == (n - 1) % 2:
                start, end, step = 0, n, 1
            else:
                start, end, step = n - 1, -1, -1
            for j in range(start, end, step):
                cells[val] = (i, j)
                val += 1

        queue = deque()
        queue.append([1, 0])
        seen = set()

        while queue:
            val, depth = queue.popleft()
            i, j = cells[val]
            print(f"processing val: {val} at depth: {depth}")
            if val == n**2:
                return depth if board[i][j] == -1 else -1

            for nxt in range(val + 1, min(val + 6, n**2) + 1):
                cell = cells[nxt]
                destination = (
                    board[cell[0]][cell[1]] if board[cell[0]][cell[1]] != -1 else nxt
                )
                if not destination in seen:
                    seen.add(destination)
                    print(f"inserting {destination} into queue from {nxt}")
                    queue.append((destination, depth + 1))
        return -1


s = Solution()
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]

print(s.snakesAndLadders(board))
