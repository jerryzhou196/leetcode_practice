# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}

        for i, e in enumerate(inorder):
            indices[e] = i

        def f(pre_s, pre_e, in_s, in_e):
            if in_s >= in_e: 
                return None

            root_val = preorder[pre_s]
            root_index = indices[root_val]
            node = TreeNode(root_val)

            # print(root_val)
            # print(preorder[pre_s:pre_e])
            # print(inorder[in_s:in_e])
            # print(root_index - in_s)

            node.left = f(pre_s + 1, 
              pre_s + 1 + root_index - in_s,
              in_s,
              root_index
            )

            node.right = f(pre_s + root_index - in_s + 1,
              pre_e,
              root_index + 1,
              in_e
            )

            return node

        return f(0, len(preorder), 0, len(preorder))




