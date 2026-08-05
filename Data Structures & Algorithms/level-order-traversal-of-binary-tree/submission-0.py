# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS with tuples:
            (node, level)
        
        when the level of the curr node increases, add the prev list to the result
        and clear out the curr level list
        """
        if not root:
            return []

        result = []
        queue = [(root, 0)]
        curr_level = 0
        curr_res = []

        while queue:
            node, level = queue.pop(0)
            if level != curr_level:
                result.append(curr_res)
                curr_res = []
                curr_level = level
            
            curr_res.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        result.append(curr_res)
        return result


