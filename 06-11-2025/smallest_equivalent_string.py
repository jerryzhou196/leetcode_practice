from collections import defaultdict

class Solution:
    def getSmallestEquivalent(self, rev, char):
        while char in rev:
            char = rev[char]
        return char
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rev = defaultdict(str)
        n = len(s1)

        for c1, c2 in zip(s1, s2):
            c1_smallest = self.getSmallestEquivalent(rev, c1)
            c2_smallest = self.getSmallestEquivalent(rev, c2)
            if c1_smallest < c2_smallest:
                rev[c2_smallest] = c1_smallest 
            elif c1_smallest > c2_smallest:
                rev[c1_smallest] = c2_smallest 

        ans = ""
        
        for char in baseStr:
            replace = self.getSmallestEquivalent(rev, char)
            ans += replace
        
        return ans

s = Solution()
# s1 = "parker", s2 = "morris", baseStr = "parser"
print(s.smallestEquivalentString("parker", "morris", "parser"))

# a = b 
# b =a






        