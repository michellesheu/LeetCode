# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        input: root of bt
        output: min depth - # of nodes on shortest path from root to leaf
        leaf - no left and right children
        empty: return 0
        root: return 1
        m: dfs recursive to traverse bt
        p:
        if not root: return 0
        if not root.left and not root.right: return height
        get left depth by dfs(left) 
        get right depth by dfs(right)
        return min(left, right) + 1 
        '''
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1
        return min(left_depth, right_depth) + 1
        