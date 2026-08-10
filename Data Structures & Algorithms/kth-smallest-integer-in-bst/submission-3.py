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
            12:29.21 - recursion
            21:24.31 - all of the above + iterative DFS w/ stack

        algo:
            - in-order traversal, return kth element
            - could use external list, or just track the recursion depth
              and return when we hit k?
            - start with external list since it's easier to reason about
        """

        """ iterative in-order traversal w/ stack
        """
        stack = []
        curr = root
        count = k

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            count -= 1
            if count == 0:
                return curr.val

            if curr:
                curr = curr.right


        """ recursion

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

        """ in order traversal

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
        