# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        
        def dfs(root, level = 0): 
            if not root: 
                return 
            
            if len(levels) == level: 
                levels.append(root.val)
            
            levels[level] = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root)
        return levels
            
            
        