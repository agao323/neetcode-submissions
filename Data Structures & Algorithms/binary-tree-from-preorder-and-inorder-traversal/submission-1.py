# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        TIME:
            1:12:18.28
                really struggling with recursion still
                    even though I understand the high level, implementation has consistently
                    been an issue. I know what I need to do but am unable to code it out
                    correctly

            1
           /   \
          2      4 (a)
         / \    /
        3   5  6 (a)
             \
              4 (b)

        a: preorder: [1, 2, 3, 5, 4, 6], inorder: [3, 2, 5, 1, 6, 4]
        b: preorder: [1, 2, 3, 5, 4], inorder: [3, 2, 5, 4, 1]

        preorder tells you the root:
            - process
            - left
            - right
        
        inorder tells you what should be left and right?:
            - left
            - process
            - right

        seems like inorder gives us the overall orientation. everything left of
        root is in the left subtree, everything right of root is the right subtree,
        and we can recursively build out the tree from there:
            [<left subtree>, current_root, <right subtree>]

        go through each node in preorder, and check inorder
            - if the next node in preorder is left of the node in inorder
                - it's a left child
            - if the next node in preorder is right of the node in inorder
                - it's a right child
        
        break this problem down into pieces
            - figure out the current root, which is just whatever element in preorder
              that we're currently checking
            - split inorder into left and right subtrees from the current root
            - go onto the next element in preorder
                - if it's in the left subtree we just made, it's a left child
                - otherwise, it's a right child
            - keep doing this until we build the tree?
        """
        inorder_indices = {node: index for index, node in enumerate(inorder)}
        self.pre_index = 0

        def dfs(left, right):
            if left >= right:
                return None

            # build this node
            val = preorder[self.pre_index]
            curr = TreeNode(val)
            self.pre_index += 1

            # build left subtree
            curr.left = dfs(left, inorder_indices[curr.val])
            # build right subtree
            curr.right = dfs(inorder_indices[curr.val] + 1, right)

            return curr
        
        return dfs(0, len(inorder))

        """
            1
           /  \
          2    4
         / \   /
        3   5 6 

        preorder: [1, 2, 3, 5, 4, 6], inorder: [3, 2, 5, 1, 6, 4]
        pre_index = 0
        left = 0, right = 6
        curr = TreeNode(1)
        curr.left = TreeNode(2)
        pre_index = 1, preorder = 2. dfs(0, 3) -> [3, 2, 5]
        curr = TreeNode(2)
        curr.left = TreeNode(3)
        curr.right = dfs(1, 3) -> [5]
            pre_index = 3, pre_order = 5
                dfs()

        pre_index = 2, pre_order = 3. dfs(0, 1) -> [3]
        curr = TreeNode(3)
        pre_index = 3, pre_order = 5. dfs(0, 0) -> [] returns

        """

        



