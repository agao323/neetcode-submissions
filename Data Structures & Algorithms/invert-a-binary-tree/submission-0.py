# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        if root.left:
            root.left = self.invertTree(root.left)
        if root.right:
            root.right = self.invertTree(root.right)
        
        temp = TreeNode(root.val, root.left, root.right)
        temp.right = root.left
        temp.left = root.right
        root = temp

        return root