class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        count = defaultdict(int)

        for y in range(n):
            for x in range(m):
                count[board[y][x]] += 1

        word_count = Counter(word)
        for char in word_count:
            if word_count[char] > count[char]: 
                return False 

        def markWord(y, x, index):
            if (y < 0 or x < 0 or y >= n or x >= m): 
                return False 
            elif board[y][x] == word[index]: 
                board[y][x] = False
                if index == len(word) - 1: 
                    return True 
                else:
                    for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        if markWord(y + i, x + j, index + 1): 
                            return True 
                board[y][x] = word[index] 

            return False 

        for y in range(n):
            for x in range(m):
                if markWord(y, x, 0):
                    return True
        return False 
                

# ["C","A","A"],
# ["A","A","A"],
# ["B","C","D"]]
  
            
            

        