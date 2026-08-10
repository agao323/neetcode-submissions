# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        TIME: 
            3:59.82 - finished BFS
            7:25.19 - finished DFS after completing BFS
        
        """

        """ DFS
            go right, then left. the first node we hit at every level
            is the right-most node for that level
        """
        result = []

        def dfs(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return None
            if len(result) <= level:
                result.append(root.val)
            
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return result

        """ level-order traversal, return last element in each level

            if not root:
                return []

            level_order = self.levelOrder(root)
            return [level[-1].val for level in level_order]
        
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            result = []
            queue = [root]
            while queue:
                result.append(queue)
                next_level = []
                for node in queue:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                queue = next_level
            
            return result
        """
