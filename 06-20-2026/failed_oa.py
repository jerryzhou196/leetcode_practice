from collections import defaultdict


class Solution:
    def getMinimumConflicts(self, primary, secondary):
        def computePrefixCount(s):
            count = [defaultdict(int)]
            for i, s in enumerate(s):
                curr_count = count[-1].copy()
                curr_count[s] += 1
                count.append(curr_count)
            return count

        p = computePrefixCount(primary)
        s = computePrefixCount(secondary)

        def getConflicts(i, j, ch):
            idx = ord(ch) - ord("a")
            ans = 0
            for c in range(25, idx, -1):
                ans += p[i][chr(c + ord("a"))]
                ans += s[j][chr(c + ord("a"))]
            return ans


# 'z' 'z' 'b' 'a'
