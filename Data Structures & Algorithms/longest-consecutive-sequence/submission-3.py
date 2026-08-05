
class ListNode:
    def __init__(self, prev: Optional[ListNode], next: Optional[ListNode], val: int):
        self.prev = prev
        self.next = next
        self.val = val

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        TIME: 18:11 for my initial O(n) solution below. beats 1.05% on runtime and 0.25% on memory

        brute force: deduplicate, sort, find longest consecutive sequence
            - O(nlogn)
        
        O(n) solution
            - build a doubly linked list?
            - each number has a prev (-1) and next (+1)
            - after building, count the longest list
            - ignore any numbers we've already seen
            - O(n) time & space to build the linked list
            - O(n) time to count the longest
        
        optimized O(n) solution (after reading answer):
            - deduplicate into set
            - no need for all this extra stuff, just figure out if an element starts a sequence by
              checking n - 1
            - track how long the sequence goes by incrementing until we don't see a number
            - much more elegant
        """
        nums = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums:
                curr = 1
                # start of a sequence
                while n + 1 in nums:
                    curr += 1
                    n += 1

                longest = max(longest, curr)
        
        return longest




        # remove duplicates
        # nums = list(set(nums))

        # num_to_node = {}
        # for n in nums:
        #     node = ListNode(None, None, n)
        #     if n - 1 in num_to_node:
        #         node.prev = num_to_node[n - 1]
        #         num_to_node[n - 1].next = node
        #     if n + 1 in num_to_node:
        #         node.next = num_to_node[n + 1]
        #         num_to_node[n + 1].prev = node
        #     num_to_node[n] = node
        
        # seen = set()
        # max_seq = 0
        # for node in num_to_node.values():
        #     if node.val in seen:
        #         continue
        #     curr_seq = 1
            
        #     seen.add(node.val)

        #     left = node
        #     while left.prev:
        #         left = left.prev
        #         curr_seq += 1
        #         seen.add(left.val)
            
        #     right = node
        #     while right.next:
        #         right = right.next
        #         curr_seq += 1
        #         seen.add(right.val)
            
        #     if curr_seq > max_seq:
        #         max_seq = curr_seq
        
        # return max_seq



