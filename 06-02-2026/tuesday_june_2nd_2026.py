from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        edges = defaultdict(list)
        costs = defaultdict(int)

        for source, dest, cost in flights:
            costs[source] = float("inf")
            costs[dest] = float("inf")
            edges[source].append([cost, dest])

        queue = deque()
        queue.append([-1, 0, src])
        costs[src] = 0

        ans = float("inf")
        while queue:
            depth, cost, node = queue.popleft()
            # print(depth, node, queue, costs)
            if depth > k:
                break

            for neighbour_cost, neighbour in edges[node]:
                if neighbour_cost + cost < costs[neighbour] and (
                    depth + 1 < k or (depth + 1 <= k and neighbour == dst)
                ):
                    costs[neighbour] = neighbour_cost + cost
                    queue.append([depth + 1, cost + neighbour_cost, neighbour])

        return costs[dst] if dst in costs and costs[dst] != float("inf") else -1


if __name__ == "__main__":
    s = Solution()

    # Example 1: expect 500
    print(
        s.findCheapestPrice(
            5, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1], [3, 4, 1]], 0, 2, 2
        )
    )

    # Example 2: expect 200
    print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))

    # Example 3: expect 699
    print(
        s.findCheapestPrice(
            3,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
        )
    )
