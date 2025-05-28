from typing import *
from collections import defaultdict

class Solution:
    def pruneZeroDegs(self, deg, adjacency_matrix, reverse_adjacency_matrix): 
        ans = set()
        for i, node in enumerate(deg): 
            if node == 0: 
                ans.add(i)

        for element in ans: 
            # [[0,1], [0,2]]
            # [[1, 0], [2, 0]]

            for node in adjacency_matrix[element]:
                deg[node] -= 1

            for node in reverse_adjacency_matrix[element]:
                deg[node] -= 1
            
            deg[element] = -1
    
        return ans
        

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        deg = [0 for _ in range(len(colors))]
        # adjacency_matrix = defaultdict(list)
        adjacency_matrix = defaultdict(list)
        reverse_adjaceny_matrix = defaultdict(list)

        for x, y in edges: 
            adjacency_matrix[x].append(y)
            reverse_adjaceny_matrix[y].append(x)
            
            deg[y] += 1
        
        zero_degs = self.pruneZeroDegs(deg, adjacency_matrix, reverse_adjaceny_matrix)
        color_count = defaultdict(int)
        while zero_degs:
            unique_colors = set()
            for index in zero_degs: 
                unique_colors.add(colors[index])
            
            for color in unique_colors: 
                color_count[color] += 1

            zero_degs = self.pruneZeroDegs(deg, adjacency_matrix, reverse_adjaceny_matrix)

        if any([val != -1 for val in deg]): return -1

        return max([count for _, count in color_count.items()])


# colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
s = Solution()
# colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
print(s.largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]))
