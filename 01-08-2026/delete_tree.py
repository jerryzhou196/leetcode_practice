class TreeNode:
    def __init__(self, val, left, right, node):
        self.val = val
        self.left = left
        self.right = right
        self.node = node 

class Node: 
    def __init__(self, val, left, right):
        self.val = val 
        self.next = left
        self.prev = right

class Tree:
    def __init__(self):

        self.root = TreeNode(-float('inf'), None, None, None)
        end = Node(float('inf'), None, None)

        self.start = Node(float('-inf'), end, None)
        end.prev = self.start

        self.root.node = self.start 

    def insert(self, val):
        def dfs(root):
            if not root: 
                node = Node(val, None, None)
                return TreeNode(val, None, None, node)
            if val < root.val:
                root.left = dfs(root.left)
            elif val > root.val:
                root.right = dfs(root.right)

            return root
        self.root = dfs(self.root)

    def getk(self, k):
        start = self.start.next
        for _ in range(k):
            start = start.next
        return start.val
    
    def delete(self, val):
        def succ(root):
            curr = root.right
            while curr.left: 
                curr = curr.left
            return curr

        def pred(root):
            curr = root.left
            while curr.right:
                curr = curr.right
            return curr
    
        def r_delete(root, key):
            if not root: return None
            if key < root.val:
                root.left = r_delete(root.left, key)
            elif key > root.val:
                root.right = r_delete(root.right, key)
            else:
                if not root.left and not root.right:
                    node = root.node
                    prev_node = node.prev
                    next_node = node.next

                    prev_node.next = next_node
                    next_node.prev = prev_node

                    return None
                elif root.left:
                    root.val = pred(root.left).val
                    root.node.val = pred(root.left).val
                    root.left = r_delete(root.left, root.val)
                else:                    
                    root.val = pred(root.right).val
                    root.node.val = succ(root.right).val
                    root.right = r_delete(root.right, root.val)
            return root

        r_delete(self.root, val)
        

c = Tree()
c.insert(4.5)
c.insert(3)
c.insert(7)
c.insert(2)
c.insert(4)
c.insert(7)
c.insert(8)
c.insert(6)
print(c.getk(4))
print(c.getk(7))

