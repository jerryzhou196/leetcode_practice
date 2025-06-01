from dataclasses import dataclass
from collections import deque
from typing import *
from copy import copy


@dataclass
class Node:
    i: int
    j: int
    depth: int


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def mapItem(val):
            """
            maps numerical val to row i, column j
            """
            i = n - 1 - (val // n)
            remainder = val % n
            if i % 2 == ((n - 1) % 2):
                return i, remainder - 1
            else:
                return i, n - 1 - remainder - 1

        def getNext(i, j):
            """
            jncrements row j, column i accordjngly
            """
            if i % 2 == ((n - 1) % 2):
                if j < n - 1:
                    return i, j + 1
                else:
                    return i - 1, j
            else:
                if j == 0:
                    return i - 1, 0
                else:
                    return i, j - 1

        queue = deque()
        queue.append(Node(n - 1, 0, 0))
        seen = set()

        while queue:
            node: Node = queue.popleft()
            jump = None
            next = [node.i, node.j]
            if node.i == 0 and node.j <= 0:
                return node.depth
            for _ in range(7):
                jump_val = board[next[0]][next[1]]
                if jump_val != -1:
                    jump = mapItem(jump_val)
                    queue.append(Node(jump[0], jump[1], node.depth + 1))
                next = getNext(next[0], next[1])

            queue.append(Node(jump[0], jump[1], node.depth + 1))


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
