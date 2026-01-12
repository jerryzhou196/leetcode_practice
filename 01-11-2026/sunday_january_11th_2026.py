from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = 0
        def find(arr):
            nonlocal index
            if index >= len(preorder):
                return -1, -1
            for i, item in enumerate(arr):
                if item == preorder[index]: 
                    index += 1
                    return i, item 
            return -1, -1

        def buildTree(left, right, val):
            nonlocal index
            # print(val, left, right, index)
            root = TreeNode(val, None, None)

            i, val = find(left)
            if i >= 0:
                root.left = buildTree(left[:i], left[i + 1:], val)
            
            i, val = find(right)
            if i >= 0:
                root.right = buildTree(right[:i], right[i + 1:], val)

            return root

        i, val = find(inorder)
        return buildTree(inorder[:i], inorder[i + 1:], val) if i >= 0 else None


            

        