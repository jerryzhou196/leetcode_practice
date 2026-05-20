# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []
        if not root: return ''
        queue, next_level = deque(), deque()
        print(not any([None,None]))

        queue.append(root)
        while True:
            while queue:
                e = queue.popleft()
                arr.append(e.val if e else None)
                if e:
                    next_level.append(e.left)
                    next_level.append(e.right)
            
            # print([g.val if g else g for g in queue], [g.val if g else g for g in next_level])
            if not next_level or (not any(next_level)):
                # print(",".join(map(str, arr)))
                return ",".join(map(str, arr))
            
            queue = next_level
            next_level = deque()

    def deserialize(self, data): 
        arr = []
        if not data: return None
        for val in data.split(','):
            if val != 'None':
                arr.append(int(val))
            else:
                arr.append(None)
        n = len(arr)
        if not data: return None
        queue, next_level = deque(), deque()
        curr = 1
        ans = TreeNode(arr[0])
        queue.append(ans)
        while True:
            while queue:
                e = queue.popleft()
                if e:
                    if curr < n and arr[curr] != None:
                        e.left = TreeNode(arr[curr])
                    curr += 1
                    if curr < n and arr[curr] != None:
                        e.right = TreeNode(arr[curr])
                    curr += 1
                    next_level.append(e.left)
                    next_level.append(e.right)

            # print(curr, [g.val if g else g for g in queue], [g.val if g else g for g in next_level])
            # print(next_level)
            if len(next_level) == 0: return ans
        
            queue = next_level
            next_level = deque() 
        


        
        
