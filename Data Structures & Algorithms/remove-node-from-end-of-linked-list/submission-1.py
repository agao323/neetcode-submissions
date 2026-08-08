# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        TIME: 
            5:47.50
        """

        """
        optimized - dummy node + two pointer
        """
        dummy = ListNode(-1)
        dummy.next = head

        right = dummy
        while n > 0:
            right = right.next
            n -= 1
        
        left = dummy
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next


        """
        figure out the length of the list
        move forward length - n
        remove that node
        O(n) time, O(1) space. can we do better?

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        diff = length - n - 1

        if diff < 0:
            return head.next

        curr1 = head
        while diff:
            curr1 = curr1.next
            diff -= 1
        curr1.next = curr1.next.next

        return head
        """