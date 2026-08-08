"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        TIME: 41:04.68
            - pretty bad, didn't realize I could hash the classes
            - I need to get better at debugging by reasoning through the code
              instead of printing statements everywhere. need to think
            - probably spend a good 30-40 min understanding all the solutions
              after the initial accepted submission

        store the original list into an array with the indices
        [(Node(3), 0), (Node(7), 1), etc.]
        this gives us the true position of the random node
        then we can correctly reconstruct the deep copy

        2 passes: store them in an array
            1. create deep copies
            2. go through and assign the next and random pointers
               to the new deep copies
        """


        """ 
        one-pass hashmap
        """
        from collections import defaultdict
        old_to_copy = defaultdict(lambda: Node(0))
        old_to_copy[None] = None

        curr = head
        while curr:
            old_to_copy[curr].val = curr.val
            old_to_copy[curr].next = old_to_copy[curr.next]
            old_to_copy[curr].random = old_to_copy[curr.random]
            curr = curr.next
        
        return old_to_copy[head]



        """
        if not head:
            return None

        curr = head
        count = 0
        node_dict = {}

        while curr:
            node_dict[curr] = count
            count += 1
            curr = curr.next

        arr1 = []
        curr2 = head
        while curr2:
            arr1.append(curr2)
            curr2 = curr2.next
        
        arr = []
        curr1 = head
        while curr1:
            arr.append(Node(curr1.val, None, None))
            curr1 = curr1.next
        
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i].next = None
            else:
                arr[i].next = arr[i + 1]
            random_node = arr1[i].random
            if random_node:
                arr[i].random = arr[node_dict[random_node]]
        
        return arr[0]
        """    
