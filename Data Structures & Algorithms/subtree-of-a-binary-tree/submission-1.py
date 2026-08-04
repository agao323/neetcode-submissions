# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Brute Force
        # traverse through root tree
        # every time there's a node with subRoot tree's root val, check the subtree
        # O(n^2) time complexity

        # Optimized - check the tree while traversing it. But how?
        root_serialized = self.serialize(root)
        subRoot_serialized = self.serialize(subRoot)

        print(root_serialized)
        print(subRoot_serialized)

        return subRoot_serialized in root_serialized
    

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "$#"
        
        return f"${root.val}{self.serialize(root.left)}{self.serialize(root.right)}"
