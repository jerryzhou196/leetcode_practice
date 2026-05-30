class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nodes = {}
        ans = []

        def traverse(curr): 
            while curr in nodes and nodes[curr]:
                neighbour = heappop(nodes[curr])
                traverse(neighbour)
            ans.append(curr)

        for node, ticket in tickets: 
            if node not in nodes: 
                nodes[node] = [ticket] 
            else: 
                heappush(nodes[node], ticket)
        
        traverse("JFK")

        return ans[::-1]
