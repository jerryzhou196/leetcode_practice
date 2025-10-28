class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rev(curr, k):
    # reverses first k edges
    prev = None
    while k > 0:
        temp = curr.next
        curr.next = prev
        curr = temp
    return curr

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    count = k
    curr = head
    while count > 0:
        count -= 1
        curr = curr.next
    res = rev(head, k - 1)
    head.next = metaRev(curr, k)
    return res