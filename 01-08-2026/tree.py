class TreeNode:
    def __init__(self, val, left, right, node):
        self.val = val
        self.left = left
        self.right = right
        self.node = None

class Node: 
    def __init__(self, val, left, right):
        self.val = val 
        self.next = left
        self.prev = right

class Tree:
    def __init__(self):
        self.root = TreeNode(None, None, None, None)
        self.start = Node(None, None, None)

    def insert(self, val):
        def dfs(root):
            if not root: return TreeNode(val, None, None, Node(val, None, None))
            if val < root.val:
                root.left = dfs(root.left)

                root_node = root.node
                new_node = root.left.node
                left_node = root_node.prev 

                root_node.prev = new_node
                new_node.next = root_node

                left_node.next = new_node
                new_node.prev = left_node
            elif val > root.val:
                root.right = dfs(root.right)

                root_node = root.node
                new_node = root.right.node
                right_node = root_node.next

                root_node.next = new_node
                new_node.prev = root_node

                right_node.prev = new_node
                new_node.next = right_node 

            return root

    def getk(self, k):
        start = self.start 
        for _ in range(k):
            start = start.next
        return start.val
    
    def delete(self, val):
        def dfs(root):
            
