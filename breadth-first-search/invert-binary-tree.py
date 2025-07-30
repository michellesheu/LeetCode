# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        input: root of binary tree
        output: return root of inverted binary tree
        can have empty tree
        match: preorder dfs, use recursion to reverse left and right subtrees of curr node
         2
        / \
        1  3
        if not root:
            return
        root.right = invertTree(root.left)
        root.left = invertTree(root.right)
        return root
        '''
        if not root:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root