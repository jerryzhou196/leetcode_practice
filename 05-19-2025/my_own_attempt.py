from collections import defaultdict


class Solution:
    def base3ToBase10(self, arr):
        val = 0
        for i in range(len(arr) - 1, -1, -1):
            power = len(arr) - (i + 1)
            val += arr[i] * (3**power)

        return val

    def colorTheGrid(self, m: int, n: int) -> int:
        valid_configurations = []

        # valid configurations
        for i in range(3**m):
            row = []
            val = i
            for _ in range(m):
                row.append(val % 3)
                val //= 3
            print(row)

            if any(row[i] == row[i + 1] for i in range(m - 1)):
                continue
            valid_configurations.append(row)

        adjacent = defaultdict(list)

        # print(self.base3ToBase10([2, 1, 0]))

        # adjacent arrays
        for row1 in valid_configurations:
            for row2 in valid_configurations:
                if any(row1[i] == row2[i] for i in range(m)):
                    continue
                adjacent[tuple(row1)].append(row2)

        prev_row = {}
        for row in valid_configurations:
            prev_row[tuple(row)] = 1

        for i, row in enumerate(valid_configurations):
            curr_row = defaultdict(int)
            for next_row in adjacent[tuple(row)]:
                curr_row[tuple(row)] += prev_row[tuple(next_row)]

            prev_row = curr_row

        print(prev_row)

        return sum(prev_row)


s = Solution()
print(s.colorTheGrid(1, 2))
