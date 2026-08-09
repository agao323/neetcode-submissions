# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        TIME: 14:44.48
            - implementation is still messy. need to clean it up a bit
            - need to practice recursion version

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
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return dummy.next

