# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # if there's a left, minimum diameter is 1
        # if there's also a right, min diameter is 2
        # find the max depth of left and right
        # add max depths to get max diameter

        max_left = self.max_depth(root.left)
        max_right = self.max_depth(root.right)
        return max(
            max_left + max_right, 
            max(
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right)
            )
        )
    
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
