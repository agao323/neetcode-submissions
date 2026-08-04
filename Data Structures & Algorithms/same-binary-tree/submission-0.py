# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q1_output = [p], []
        while q1:
            curr = q1.pop(0)

            if curr:
                q1_output.append(curr.val)
                q1.append(curr.left)
                q1.append(curr.right)
            else:
                q1_output.append(None)


        q2, q2_output = [q], []
        while q2:
            curr = q2.pop(0)

            if curr:
                q2_output.append(curr.val)
                q2.append(curr.left)
                q2.append(curr.right)
            else:
                q2_output.append(None)
        
        return q1_output == q2_output
        

