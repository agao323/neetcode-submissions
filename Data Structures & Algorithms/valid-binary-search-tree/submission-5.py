import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        TIME: 20:40.30
            - solved using in-order traversal with an extra output array
              but probably not the most efficient solution
        TIME: 27:06 for DFS solution
        TIME: idk but only took a few minutes to code up BFS. maybe like 30:00?

        base case: left < root < right
        then recurse left and right
        left and right subtrees need to return the max value found
        then need to compare the max in each subtree to current root
        """

        """ bfs solution

        algo:
            - same thing as dfs, just using a queue and tracking
              max left and right within the queue
        """
        from collections import deque
        
        queue = deque([(root, -math.inf, math.inf)])
        
        while queue:
            curr, left, right = queue.popleft()
            if not left < curr.val < right:
                return False
            if curr.left:
                queue.append((curr.left, left, curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, right))
        
        return True


        """ dfs solution

        algo:
            - at each point, narrow the possible range of values
              root can contain by managing a left and right max
        return self.dfs(root, -math.inf, math.inf)
    
    def dfs(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        if not root:
            return True
        
        if not left < root.val < right:
            return False
        
        # in left subtree, max range is capped so pass root into right
        l_subtree = self.dfs(root.left, left, root.val)
        # in right subtree, min range is capped so pass root into left
        r_subtree = self.dfs(root.right, root.val, right)
        return l_subtree and r_subtree
        """




        """ in-order traversal solution

        out = []

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            out.append(root.val)
            if root.right:
                dfs(root.right)

        dfs(root)
        if len(out) <= 1:
            return True
        
        for i in range(1, len(out)):
            if out[i-1] >= out[i]:
                return False

        return True
        """
        

        




