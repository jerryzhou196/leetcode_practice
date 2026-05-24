class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        def find(a):
            while a != parent[a]:
                parent[a] = find(parent[a])
            return a

        def union(a,b):
            parent[find(a)] = find(b)

        for num in nums: 
            union(num, num)
            if num - 1 in s: 
                union(num - 1, num - 1)
                union(num, num - 1)
            if num + 1 in s: 
                union(num + 1, num + 1)
                union(num, num + 1)

        print(parent)

longestConsecutive()
