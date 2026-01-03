# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        left, right = self.getHeight(root.left), self.getHeight(root.right)
        return False if abs(left - right) > 1 else True

        