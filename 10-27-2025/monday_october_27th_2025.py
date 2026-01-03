ans = 0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def maxDepth(root):
            if not root: return 0
            nonlocal ans 
            left = 1 + maxDepth(root.left) if root.left else 0
            right = 1 + maxDepth(root.right) if root.right else 0
            ans = max(ans, left + right)
            return max(left, right) 
        
        maxDepth(root)
        return ans
    