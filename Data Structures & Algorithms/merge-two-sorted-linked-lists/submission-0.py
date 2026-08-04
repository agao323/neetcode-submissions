# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        curr1 = list1
        curr2 = list2

        head = None
        if list1.val <= list2.val:
            head = list1
            curr1 = head.next
        else:
            head = list2
            curr2 = head.next
        ret = head
        
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    head.next = curr1
                    curr1 = curr1.next
                else:
                    head.next = curr2
                    curr2 = curr2.next
            elif curr1:
                head.next = curr1
                curr1 = curr1.next
            else:
                head.next = curr2
                curr2 = curr2.next
            
            head = head.next

        return ret
            