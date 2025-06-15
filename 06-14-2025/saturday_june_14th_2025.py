from heapq import *
class Solution:
    def clearStars(self, s: str) -> str:
        smallest = []
        input_string = list(s)

        for i, char in enumerate(input_string):
            if char == '*':
                val, index = heappop(smallest)
                input_string[-1 * index] = ''
                input_string[i] = ''
            else:
                heappush(smallest, (char, -i))
        
        return "".join(input_string)
    