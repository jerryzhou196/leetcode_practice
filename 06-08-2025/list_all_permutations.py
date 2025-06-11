def splitString(s):
    n = len(s)

total = set()
unique_strings = set()

def generatePermutation(s, arr):
    ans = []
    group = []
    for i, e in enumerate(s):
        group.append(e)
        if i < len(s) - 1 and arr[i] == 1:
            ans.append(group)
            group = []

    if group:
        ans.append(group)

    for e in ans:
        unique_strings.add(tuple(e))

    total.add(tuple([tuple(e) for e in ans]))

def printAllSplits(s, groups):
    n = len(s)
    arr = [0] * (n - 1)
    
    def generateStr(pos, totalCount, arr):
        if totalCount == 0:
            generatePermutation(s, arr)
        elif pos < n: 
            if pos < n - 1:
                arr[pos] = 1
            generateStr(pos + 1, totalCount - 1, arr)
            if pos < n - 1:
                arr[pos] = 0
            generateStr(pos + 1, totalCount, arr)

    return generateStr(0, groups - 1, arr)

printAllSplits("dbca", 2)
print(f"len(ans): {len(total)}")
for s in total:
    print(s)

with open('output', 'w') as f:
    f.write(str(total))

with open('unique_elements', 'w') as f:
        f.write(str(sorted(unique_strings)))