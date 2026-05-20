class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        ans = []

        trie = {}
        for word in words:
            curr = trie
            for c in word: 
                curr = curr.setdefault(c, {})
            curr['$'] = word

        def dfs(curr_y, curr_x, node): 
            nonlocal ans 
            if curr_y < 0 or curr_y >= m or curr_x < 0 or curr_x >= n or board[curr_y][curr_x] == 'X':
                return 
            
            parent = node
            if board[curr_y][curr_x] in node: 
                node = node[board[curr_y][curr_x]]
                # print(node, board[curr_y][curr_x], parent)
                if '$' in node:
                    ans.append(node['$'])
                    del node['$']

                letter = board[curr_y][curr_x]
                board[curr_y][curr_x] = 'X' 
                for diff_y, diff_x in [[0, 1], [1, 0], [-1 ,0], [0, -1]]:
                    new_y, new_x = curr_y + diff_y, curr_x + diff_x
                    dfs(new_y, new_x, node)
                board[curr_y][curr_x] = letter

                if not node: 
                    del parent[letter]

            return False

        for y in range(m):
            for x in range(n):
                dfs(y, x, trie)
        
        return list(set(ans))

    
    # [["a","b","c"],
    #  ["a","e","d"],
    #  ["a","f","g"]]



