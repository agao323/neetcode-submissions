# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        algo:
            - in-order traversal, return kth element
            - could use external list, or just track the recursion depth
              and return when we hit k?
            - start with external list since it's easier to reason about
        """

        elements = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            elements.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return elements[k - 1]
        