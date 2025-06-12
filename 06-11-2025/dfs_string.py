from collections import defaultdict

class Solution:
    def getSmallestEquivalent(self, rev, char):
        while char in rev:
            char = rev[char]
        return char
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        edges = defaultdict(list)
        for c1, c2 in zip(s1, s2):
            edges[c1].append(c2)
            edges[c2].append(c1)

        replace = defaultdict(str)
        seen = set()

        def dfs(char, group):
            group.add(char)
            for neighbour in edges[char]:
                if neighbour not in group:
                    dfs(neighbour, group)
        
        for char in s1:
            group = set()
            dfs(char,group)
            smallest = min(group)
            for char in group:
                replace[char] = smallest
            seen.update(group)
        
        print(replace)
        
        ans = ""
        for char in baseStr:
            if char in replace:
                ans += replace[char]
            else:
                ans += char
        return ans
    
s = Solution()
# s1 = "parker", s2 = "morris", baseStr = "parser"
print(s.smallestEquivalentString("parker", "morris", "parser"))
        