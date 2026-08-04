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

        return self.recurse(root, 1)
    
    def recurse(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return depth - 1
        
        return max(self.recurse(node.left, depth + 1), self.recurse(node.right, depth + 1))



