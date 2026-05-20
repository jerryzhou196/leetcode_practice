# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_index = 0

        indices = {}
        for i, v in enumerate(inorder):
            indices[v] = i

        def f(left, right):
            if left >= right: 
                return None


            nonlocal root_index
            root = TreeNode(preorder[root_index])
            root_location = indices[preorder[root_index]]
            root_index += 1

            root.left = f(left, root_location)
            root.right = f(root_location + 1, right)
            return root
        
        return f(0, len(preorder))

            
        