root of a binary tree: 

                2 (0)
        1 (-1)              3 (1)
    -2 (-2)     2 (0)   3 (0)    4 (2)

ans = {}
def verticalTree(root, curr_val):
    if not root: return 
    ans[curr_val].append(root.val)
    verticalTree(root.left, curr_val - 1)
    verticalTree(root.left, curr_val + 1)

ans = []
for key, items in ans.items():
    heapq.heappush(ans, [key, items])

return [e for key, e in ans]
    






    

    
