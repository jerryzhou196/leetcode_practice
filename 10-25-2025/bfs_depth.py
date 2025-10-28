# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        ans = 0
        queue.append([root, 0])
        while queue:
            node, depth = queue.popleft()
            if node:
                ans = max(depth + 1, ans)
                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])
        return ans


        