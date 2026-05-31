class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, points[0])]
        seen = set()
        cost = 0

        while len(seen) < len(points): 
            # print(heap, seen)
            val, point = heappop(heap)
            y, x = point
            if (y, x) in seen: continue 
            cost += val
            seen.add((y,x))

            for i, j in points:
                if not (i == y and j == x): 
                    heappush(heap, (abs(y - i) + abs(x - j), [i, j]))


        return cost 
           
