class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        # edges = defaultdict(list)
        for i, (y, x) in enumerate(edges, 1):
            parent[i] = i 
            # edges[y] = x

        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            root = find(a)
            root1 = find(b)
            parent[root] = root1

        for a, b in edges:         
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)

