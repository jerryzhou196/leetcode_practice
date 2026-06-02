class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words) 
        edges = defaultdict(list) 
        indegree = defaultdict(int)
        def addEdge(word1, word2): 
            i = 0
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]: 
                i += 1
            return word1[i] if i < len(word1) else None, word2[i] if i < len(word2) else None

        for word in words:
            for c in word: 
                indegree[c] = 0
            
        for i in range(n - 1): 
            x, y = addEdge(words[i], words[i + 1])
            if x != None and y != None: 
                edges[x].append(y)
            elif not y and x: return ""
            if y and x: indegree[y] += 1
        
        ans = ""
        queue = deque([node for node in indegree if indegree[node] == 0])
        while queue:
            node = queue.popleft()
            ans += node
            for neighbour in edges[node]: 
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0: 
                    queue.append(neighbour)
        
        return ans if len(ans) == len(indegree) else ""
          
