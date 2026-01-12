class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            nodes[a].append((b,  values[i]))
            nodes[b].append((a,  1 / values[i]))
        
        ans = []
        def dfs(curr, end, prev, seen):
            if curr == end: return 1
            if curr in seen or curr not in nodes: return 0
            seen.add(curr)
            for neighbour, val in nodes[curr]:
                res = val * dfs(neighbour, end, curr, seen)
                if res != 0:
                    return res
            return 0
        
        for start, end in queries:
            new_set = set()
            res = dfs(start, end, None, new_set)
            ans.append(res if (start in nodes and res > 0) else -1)

        return ans
