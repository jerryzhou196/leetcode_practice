class Solution:
    def clearStars(self, s: str) -> str:
        input_string = list(s)
        largest_index = 0

        for i, char in enumerate(input_string):
            if char == '*':
                input_string[largest_index] = ''
                input_string[i] = ''
                largest_index = i + 1
            elif char < input_string[largest_index]:
                largest_index = i
            elif char == input_string[largest_index]: 
                largest_index = i
        
        return "".join(input_string)
    

s = Solution()
s.clearStars("aaba*")
