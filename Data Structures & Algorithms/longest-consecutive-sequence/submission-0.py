
class ListNode:
    def __init__(self, prev: Optional[ListNode], next: Optional[ListNode], val: int):
        self.prev = prev
        self.next = next
        self.val = val

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        brute force: deduplicate, sort, find longest consecutive sequence
            - O(nlogn)
        
        O(n) solution
            - build a doubly linked list?
            - each number has a prev (-1) and next (+1)
            - after building, count the longest list
            - ignore any numbers we've already seen
            - O(n) time & space to build the linked list
            - O(n) time to count the longest
        """
        # remove duplicates
        nums = list(set(nums))

        num_to_node = {}
        for n in nums:
            node = ListNode(None, None, n)
            if n - 1 in num_to_node:
                node.prev = num_to_node[n - 1]
                num_to_node[n - 1].next = node
            if n + 1 in num_to_node:
                node.next = num_to_node[n + 1]
                num_to_node[n + 1].prev = node
            num_to_node[n] = node
        
        seen = set()
        max_seq = 0
        for node in num_to_node.values():
            if node.val in seen:
                continue
            curr_seq = 1
            
            left = node
            while left.prev:
                left = left.prev
                curr_seq += 1
            
            right = node
            while right.next:
                right = right.next
                curr_seq += 1
            
            if curr_seq > max_seq:
                max_seq = curr_seq
        
        return max_seq



