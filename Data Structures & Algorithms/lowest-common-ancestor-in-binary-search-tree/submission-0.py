# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        want to find the LCA. that means we need the first node where we've recursed
        through the tree and found both p and q

        recursion definition
            - if root is p or q, that should be a stopping point
                - that's not true. p or q can be below each other
            - if root is null, that should stop
            - we should track whether we've found p or found q
            - as soon as we've found both, we can return that node

        2 options:
            1. a node is the LCA but is not p or q
            2. a node is p/q and is LCA

        algo:
            - if None, return
            - if p or q, set return to p or q
            - recurse left and right
            - each recursion layer should return either:
                - p, q, or the lca
            - if both children return something, current node is LCA
            - if nothing is returned from children, we can move on
        """
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        return dfs(root)













