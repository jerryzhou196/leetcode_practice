import heapq

class Solution:
    def minInterval(self, A, queries):
        A = sorted(A)[::-1]
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]


if __name__ == "__main__":
    s = Solution()

    # Basic case: query inside interval, query outside
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    print(s.minInterval(intervals, queries))  # expected: [3, 3, 1, 4]

    # Single interval covers all queries
    intervals = [[1, 10]]
    queries = [3, 7, 1]
    print(s.minInterval(intervals, queries))  # expected: [10, 10, 10]

    # Query not covered by any interval
    intervals = [[2, 3], [5, 8]]
    queries = [1, 4, 9]
    print(s.minInterval(intervals, queries))  # expected: [-1, -1, -1]

    # Multiple intervals, pick smallest covering
    intervals = [[1, 3], [1, 10], [2, 4]]
    queries = [2]
    print(s.minInterval(intervals, queries))  # expected: [3]
