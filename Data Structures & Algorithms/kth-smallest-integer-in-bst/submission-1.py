# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        TIME:
            2:19.01 - in order traversal with external list

        algo:
            - in-order traversal, return kth element
            - could use external list, or just track the recursion depth
              and return when we hit k?
            - start with external list since it's easier to reason about
        """
        n, res = k, root.val

        def dfs(node):
            nonlocal n, res
            if not node:
                return
            
            dfs(node.left)
            if n == 0:
                return
            n -= 1
            if n == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res

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
        """
        