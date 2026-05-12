# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        def f(node):
            if not node: 
                return -float('inf'), 0
            
            completeL, openL = f(node.left)
            completeR, openR = f(node.right)

            print(node.val, completeL, completeR)

            complete = max(completeR, completeL, openL + node.val + openR, node.val)
            o = max(openL, openR, 0) + node.val

            return complete, o 
        
        a,b = f(root)
 
        return max(a,b)


which of the following is true regarding the policy evaluation?


1. we must use synchrnous backups for the policy evaluation 
2. we can iteratively apply the bellman expectation backup equation to obtain the value function for a given policy pi 
3. asynchrnous backups are not allowed for the policy evaluation 
4. the policy evaluation is needed in both the prediction problem (i.e. predicting the value function, and the control problem (i.e. finding the optimal control policy))
