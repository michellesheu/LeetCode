# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case: If root is None or matches p or q, return root
        if not root or root == p or root == q:
            return root

        # Recurse left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, current root is the LCA
        if left and right:
            return root

        # If only one is not None, return the non-None side
        return left if left else right

        