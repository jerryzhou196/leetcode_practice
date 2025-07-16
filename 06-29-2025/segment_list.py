from typing import *

class SegmentListNode:
    def __init__(self, left, right, start, end, min):
        self.left: SegmentListNode | None = left
        self.right: SegmentListNode | None = right
        self.start: int = start
        self.end: int = end
        self.min: int = min

def createSegmentList(left, right, nums):
    node = SegmentListNode(None, None, left, right, 0)
    if left > right: 
        node.left = right
        node.min = right
        return node
    
    if left == right:
        node.min = left 
    else:
        m = (left + right) // 2
        node.left, node.right = createSegmentList(left, m, nums), createSegmentList(m + 1, right, nums)
        if nums[node.left.min] < nums[node.right.min]:
            node.min = node.left.min 
        else:
            node.min = node.right.min 
    
    return node

def searchSegmentList(root, search_left, search_right, nums):
    print(root.start, root.end, root.min)
    # [root.left, root.right] must be a subset of [search_left, search_right]
    if (root == None or search_left > root.end or search_right < root.start):
        return -1
    if (root.start >= search_left and root.end <= search_right):
        return root.min

    leftmin = searchSegmentList(root.left, search_left, search_right, nums)
    rightmin = searchSegmentList(root.right, search_left, search_right, nums)
    print(f"leftmin: {leftmin}, rightmin: {rightmin}")
    if leftmin == -1: return rightmin
    if rightmin == -1: return leftmin 
    return leftmin if nums[leftmin] < nums[rightmin] else rightmin

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        node = createSegmentList(0, len(heights) - 1, heights)

        def helper(left, right):
            if left >= right:
                return heights[left]
            minIndex = searchSegmentList(node, left, right, heights)
            return max(
                helper(left, minIndex - 1),
                helper(minIndex + 1, right),
                (right - left + 1) * heights[minIndex] 
            )
        
        return helper(0, len(heights))
            

arr = [2,1,5,6,2,3]
s = Solution()
s.largestRectangleArea(arr)