from copy import copy


class Solution:
    def analyzeGroup(self, group, limit):
        curr_group_size = 0

        groups_violated = 0

        for char in group:
            if char == "|":
                if curr_group_size > limit:
                    groups_violated += 1
                curr_group_size = 0
            else:
                curr_group_size += 1

        if curr_group_size > limit:
            groups_violated += 1

        return groups_violated

    def listAllPermutations(self, n) -> int:
        total = []
        permutation = ["*"] * (n + 2)

        for i in range(n + 2):
            permutation[i] = "|"
            for j in range(i + 1, n + 2):
                permutation[j] = "|"
                total.append((copy(permutation), self.analyzeGroup(permutation, 2)))
                permutation[j] = "*"
            permutation[i] = "*"

        for e in sorted(total, key=lambda x: x[1]):
            print(e)

        return total


s = Solution()
print(len(s.listAllPermutations(10)))
print(len(s.listAllPermutations(7)))
