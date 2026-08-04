# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class QueueItem:
    def __init__(self, node: Optional[TreeNode], depth: int):
        self.node = node
        self.depth = depth

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [QueueItem(root, 1)]
        max_depth = 1

        while q:
            curr = q.pop(0)
            max_depth = max(max_depth, curr.depth)
            if curr.node.left:
                q.append(QueueItem(curr.node.left, curr.depth + 1))
            if curr.node.right:
                q.append(QueueItem(curr.node.right, curr.depth + 1))
        
        return max_depth



        