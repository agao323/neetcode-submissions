# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Brute Force
        # traverse through root tree
        # every time there's a node with subRoot tree's root val, check the subtree
        # O(n^2) time complexity

        # Optimized - check the tree while traversing it. But how?
        if not subRoot:
            return True

        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr and curr.val == subRoot.val:
                if self.isSameTree(curr, subRoot):
                    return True
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        
        return False

    def isSameTree(self, root_1: Optional[TreeNode], root_2: Optional[TreeNode]) -> bool:
        queue = [(root_1, root_2)]

        while queue:
            curr_1, curr_2 = queue.pop(0)
            if not curr_1 and not curr_2:
                continue
            if not curr_1 or not curr_2:
                return False
            if curr_1.val != curr_2.val:
                return False
            
            queue.append((curr_1.left, curr_2.left))
            queue.append((curr_1.right, curr_2.right))
        
        return True
