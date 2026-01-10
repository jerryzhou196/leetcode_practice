class Solution:
    def decodeString(self, s: str) -> str:
        def isDigit(char):
            return ord(char) >= 48 and ord(char) <= 57

        index = [0]

        def dfs(index):
            res = ''
            while index[0] < len(s) and s[index[0]] != ']':
                # print(f"index: {index[0]}, {s[index[0]]}")
                if not isDigit(s[index[0]]):
                    res += s[index[0]]
                    index[0] += 1
                else: 
                    digit = ''
                    while isDigit(s[index[0]]):
                        digit += s[index[0]]
                        index[0] += 1
                    index[0] += 1
                    ret = dfs(index)
                    res = res + ret * int(digit)
                    index[0] += 1
            return res
        
        return dfs(index)

                    
                    

                
                    