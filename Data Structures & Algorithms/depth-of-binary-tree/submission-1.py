# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [(root, 1)]
        max_depth = 1

        while q:
            curr, curr_depth = q.pop(0)
            max_depth = max(max_depth, curr_depth)
            if curr.left:
                q.append((curr.left, curr_depth + 1))
            if curr.right:
                q.append((curr.right, curr_depth + 1))
        
        return max_depth



