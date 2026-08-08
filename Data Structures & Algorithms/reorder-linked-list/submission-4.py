# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        TIME:
            ~11:50 for initial solution

        stack?
        go through the list and push nodes onto the stack
        figure out the length (and stopping point) from size of stack
        go back to the head and start reordering the nodes

        O(1) space is required, so must be something else
        reverse the second half?
        0 > 1 > 2 > 3 < 4 < 5 < 6
        two pointers, one left one right
        alternate 0 > 6 > 1 > 5 > 2 > ...
        solution figured out ~12 min in

        2 > 4 > 6 > 8
        2 > 4 > 6 < 8

        [0, 1, 2, 3, 4]
        slow/fast = 0/1 -> 1/3 -> 
        [0, 1, 2, 3, 4, 5]
        """
    
        # find halfway point
        curr, count = head, 0
        while curr:
            count += 1
            curr = curr.next
        
        if count <= 2:
            return

        # only reverse count / 2 + 1 and onwards, but we need the first one
        mid_count = int(count / 2)
        mid = head
        while mid_count:
            mid = mid.next
            mid_count -= 1
        
        dummy = ListNode(-1)
        end_start = mid.next
        mid.next = dummy
        
        # print(f"end_start.val: {end_start.val}")
        tmp = self.reverse(end_start)
        end = tmp
        
        while tmp.next:
            tmp = tmp.next
        tmp.next = dummy

        hp = head
        ep = end

        # while ep:
        #     print(f"ep.val: {ep.val}")
        #     ep = ep.next
        # print(f"hp.val: {hp.val}")
        # print(f"ep.val: {ep.val}")

        while hp and ep and hp.next and ep.next:
            if hp.next == dummy:
                hp.next = None
            if ep.next == dummy:
                ep.next = None

            head_next = hp.next
            hp.next = ep
            hp = head_next
            end_next = ep.next
            ep.next = hp
            ep = end_next



        while head:
            if head.next.val == -1:
                head.next = None
            head = head.next

    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
            


