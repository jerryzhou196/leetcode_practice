import bisect

def findMaximumValue(prices, pos, amount):
    prefix_sum = []
    total = 0

    for price in prices:
        total += price 
        prefix_sum.append(total)

    ans = 0
    for i, start in enumerate(pos):
        start = start - 1

        res = bisect.bisect_right(prefix_sum, amount[i], start, len(prefix_sum)) 
        print(prefix_sum[start:], amount[i], res)
        ans = max(ans, res - start)
    
    return ans


prices = [3, 4, 5, 5, 7]
pos = [2, 1, 5]
amount = [10, 24, 5]
print(findMaximumValue(prices, pos, amount))
