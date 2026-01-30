# s = "leetcode", wordDict = ["leet", "code"]
# s = "applenapple", wordDict = ["apple", "pen"]
# s = "applenapple", wordDict = ["apple", "applen", "app", "len"]

O(2^n)

# iteration #1 
# a

# iteration #2
# ap

# iteration #3
# app

# iteration #4
# appl

# iteration #5
# apple

# iteration #5
# n
# applen

# iteration #5
# na
# a 
# applena

def solution(word, words): 
    def dfs(index, curr_word):
        if index == len(word):
            if curr_word in words: 
                return True
            return False

        curr_word += word[index]
        if curr_word in words: 
            dfs(index + 1, "")
        dfs(index + 1, curr_word)
    
    return dfs(0, "")
    
            




"applenapple"


