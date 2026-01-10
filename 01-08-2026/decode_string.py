class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        count_stack = []
        substr = '' 
        num = ''
        for char in s:
            print(f"char: {char}, str_stack: {str_stack}, count_stack: {count_stack}, substr: {substr}")
            if char == ']':
                last = str_stack.pop()
                last = last + substr * count_stack.pop()
                substr = last
            elif ord(char) >= 48 and ord(char) <= 57: 
                num += char
            elif char == '[':
                count_stack.append(int(num))
                str_stack.append(substr)
                substr, num = '', ''
            else:
                substr = substr + char

        return substr 
