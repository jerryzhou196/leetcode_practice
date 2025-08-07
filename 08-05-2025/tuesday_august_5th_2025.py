class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        first = ListNode(-1, None)
        ans = first
        while l1 and l2:
            ans.next = ListNode((l1.val + l2.val + carry) % 10, None)
            ans = ans.next
            print(f"ans.val {ans.val}")
            
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1: 
            ans.next = ListNode((l1.val + carry) % 10, None)
            ans = ans.next
            print(f"ans.val {ans.val}")

            carry = (l1.val + carry) // 10
            l1 = l1.next

        while l2:
            ans.next = ListNode((l2.val + carry) % 10, None)
            ans = ans.next
            print(f"ans.val {ans.val}")

            carry = (l2.val + carry) // 10
            l2 = l2.next

        if carry:
            ans.next = ListNode(carry, None)
            print(f"ans.val {ans.val}")
        
        return first.next 