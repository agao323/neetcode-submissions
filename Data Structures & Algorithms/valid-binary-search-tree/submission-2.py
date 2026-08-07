# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        base case: left < root < right
        then recurse left and right
        left and right subtrees need to return the max value found
        then need to compare the max in each subtree to current root
        
        or: just to a post-order traversal
        """
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
        

        




