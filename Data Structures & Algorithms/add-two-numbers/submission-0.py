# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        thoughts:
            - track a carry value
            - use a dummy
            - edge cases: l1/l2 is none or starts with 0
        """

        if not l1 or not l1.val:
            return l2
        if not l2 or not l2.val:
            return l1
        if not l1 and not l2:
            return None

        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit > 9:
                digit = digit % 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if not l1:
            l1, l2 = l2, l1

        while l1:
            digit = l1.val + carry
            if digit > 9:
                digit = digit % 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next

