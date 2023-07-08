def parse(tokens, parse_table, start_symbol):
    stack = [start_symbol]
    cursor = 0

    while stack:
        top = stack[-1]
        token = tokens[cursor]

        if top == token:
            stack.pop()
            cursor += 1
        else:
            production = parse_table.get((top, token))

            if production is None:
                raise SyntaxError(f"Unexpected token: {token}")

            stack.pop()

            # Push symbols of the production to the stack in reverse order
            for symbol in reversed(production):
                stack.append(symbol)

        if cursor == len(tokens) and len(stack) == 0:  # if we've reache
            print("Input is successfully parsed")
        elif cursor == len(tokens) and len(stack) > 0:
            raise SyntaxError(f"Input ended but stack is not empty")


# example usage
tokens = ["a", "a", "b", "b", "a", "a"]  # Your input to parse
parse_table = {  # Your parse table
    ("S", "a"): ["A", "S"],
    ("S", "b"): ["B", "S"],
    ("A", "a"): ["a", "A"],
    ("B", "b"): ["b", "B"],
    ("S", "$"): [],
    ("A", "$"): [],
    ("B", "$"): [],
}
parse(tokens, parse_table, "S")
