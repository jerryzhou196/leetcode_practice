def splitString(s):
    n = len(s)

total = set()

def generatePermutation(s, arr):
    ans = []
    group = []
    for i, e in enumerate(arr):
        if e == 1:
            group.append(s[i])
            ans.append(group)
            group = []
        else:
            group.append(s[i])
    if group:
        ans.append(group)
    total.add(tuple([tuple(e) for e in ans]))

def printAllSplits(s, groups):
    arr = list(s) 
    n = len(arr)
    count = [0] * n 
    
    def generateStr(pos, totalCount, arr):
        if totalCount == 0:
            generatePermutation(s, arr)
        elif pos < n: 
            arr[pos] = 1
            generateStr(pos + 1, totalCount - 1, arr)
            arr[pos] = 0
            generateStr(pos + 1, totalCount, arr)

    return generateStr(0, groups - 1, count)

printAllSplits("arcslogger", 5)
print(f"len(ans): {len(total)}")
for s in total:
    print(s)
