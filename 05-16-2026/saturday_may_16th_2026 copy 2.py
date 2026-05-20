# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, small, big):
            if not node: 
                return False
            
            if small.val <= node.val and node.val <= big.val:
                return node
            elif small.val <= node.val and big.val <= node.val:
                return dfs(node.left, small, big)
            else:
                return dfs(node.right, small, big)
            
        if p.val > q.val:
            p, q = q, p

        return dfs(root, p, q)





        return ans
            


            

        
        