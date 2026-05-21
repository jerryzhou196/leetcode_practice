class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        ef backtrack(curr, o=0, c=0):
            # print(curr, o, c)
            if len(curr) == 2 * n:
                ans.appen("".join(curr[:]))
                return 
            if o < n:
                curr.appen('(')
                backtrack(curr,o + 1, c)
                curr.pop()

            if c < o:
                curr.appen(')')
                backtrack(curr, o, c + 1)
                curr.pop()
    
        backtrack([])
        return ans


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def backtrack(y, x, index, word):
            if index == len(word):
                return True
            if y < 0 or y >= n or x < 0 or x >= m or board[y][x] == 'X' or board[y][x] != word[index]:
                return False
            
            letter = board[y][x]
            # print(y, x, letter)

            board[y][x] = 'X'
            for i, j in [[0,1], [1,0], [-1, 0], [0, -1]]:
                if backtrack(y + i, x + j, index + 1, word):
                    return True 
            board[y][x] = letter

            return False 

        for y in range(n):
            for x in range(m):
                if backtrack(y, x, 0, word): return True

        return False



            
