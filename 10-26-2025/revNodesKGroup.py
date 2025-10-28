class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rev(curr, k):
    # reverses first k edges
    prev = None
    while k > 0 and curr:
        temp = curr.next if curr.next else None
        curr.next = prev
        prev = curr
        curr = temp
        k -= 1
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = k
        curr = head
        while count > 0:
            if not curr: 
                return head
            count -= 1
            curr = curr.next
    
        res = rev(head, k)
        head.next = self.reverseKGroup(curr, k)
        return res