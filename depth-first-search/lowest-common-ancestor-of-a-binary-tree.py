# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        left = right = None
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if right and left:
            return root
        else:
            return left or right
        