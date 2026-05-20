# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        top, nextLevel = deque(), deque()
        ans = []
        if not root: return []
        top.append(root)

        while True:
            while top: 
                e = top.popleft()
                print(e.val, [n.val for n in top])
                if len(top) == 0: 
                    ans.append(e.val)
                if e.left: 
                    nextLevel.append(e.left)
                if e.right: 
                    nextLevel.append(e.right)
            
            if not nextLevel: return ans

            top = nextLevel
            nextLevel = deque()


        
               
            
            
        