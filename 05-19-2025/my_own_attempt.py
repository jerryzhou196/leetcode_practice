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
                hash = self.base3ToBase10(row1)
                adjacent[hash].append(row2)

        prev_row = {}
        for row in valid_configurations:
            prev_row[self.base3ToBase10(row)] = 1

        for _ in range(n - 1):
            curr_row = defaultdict(int)
            for i, row in enumerate(valid_configurations):
                hash = self.base3ToBase10(row)
                for next_row in adjacent[hash]:
                    curr_row[hash] += prev_row[self.base3ToBase10(next_row)]

            prev_row = curr_row

        ans = 0
        for key, val in prev_row.items(): 
            ans += val

        return ans 



s = Solution()
print(s.colorTheGrid(1, 1))
