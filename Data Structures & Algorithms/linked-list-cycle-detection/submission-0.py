# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # algorithm: two pointers, one slow one fast
        # slow increments by 1, fast increments by 2
        # if they both overlap on an index, there's a cycle
        # if they both go null, no cycle
        if not head:
            return False
            
        slow, fast = head, head.next

        while slow and fast:
            if slow.val == fast.val:
                return True
            
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next

        return False
        