class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == "+":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first) + int(second))
            elif element == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first) - int(second))
            elif element == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first) // int(second))
            elif element == "*":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first) * int(second))
            else:
                stack.append(element)

        return first
