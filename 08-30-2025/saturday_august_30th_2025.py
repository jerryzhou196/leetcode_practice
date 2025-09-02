class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def add(self, key, val):
        node = ListNode(key, val)
        self.dict[key] = node

        prev_last = self.tail.prev 
        self.tail.prev = node 
        node.next = self.tail

        node.prev = prev_last
        prev_last.next = node 

    def remove(self, key):
        node = self.dict[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.dict[key]

    def get(self, key: int) -> int:
        val = -1
        if key in self.dict:
            val = self.dict[key].val
            self.remove(key)
            self.add(key, val)
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(key)
        elif len(self.dict) == self.capacity:
            self.remove(self.head.next.key)
        self.add(key, value)