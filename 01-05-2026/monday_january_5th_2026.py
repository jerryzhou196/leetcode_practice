# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, prev_max=-float('inf')):
            if not root:
                return 0
            prev_max = max(root.val, prev_max)
            if root.val >= prev_max: 
                return 1 + dfs(root.left, prev_max) + dfs(root.right, prev_max)
            else:
                return dfs(root.left, prev_max) + dfs(root.right, prev_max)
        
        return dfs(root)

        

        