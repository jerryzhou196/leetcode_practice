def finalPrice(prices):
    total = 0
    asc_stack = []

    for i, price in enumerate(prices):
        print(asc_stack)
        while asc_stack and asc_stack[-1][1] >= price:
            _, val = asc_stack.pop()
            total += (val - price)
        asc_stack.append((i,price))

    for (i, val) in asc_stack:
        total += val
    
    print(total)

    for (i, val) in asc_stack:
        print(i)

finalPrice([2, 3, 1, 2, 4, 2])




    







    # [2, 3, 1, 2, 4, 2]
    # asc_stack: [(0, 1), (2, 1)]
    # total: 1 + 2 + 2 + 0 + 1 + 2







