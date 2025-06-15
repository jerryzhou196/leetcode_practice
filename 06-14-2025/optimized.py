from heapq import *
class Solution:
    def clearStars(self, s: str) -> str:
        chars = [[] for _ in range(26)]
        input_string = list(s)

        for i, char in enumerate(s):
            if char == '*':
                for j in range(26):
                    if len(chars[j]) > 0:
                        input_string[chars[j].pop()] = ''
                        break
                input_string[i] = ''
            else:
                input_string[ord(char) - ord('a')].append(i)
        
        return "".join(input_string)
