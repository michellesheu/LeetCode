# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_child, right_child, level):
            if not left_child or not right_child:
                return
            # if even level, reverse children in odd level
            if level % 2 == 0:
                temp = left_child.val
                left_child.val = right_child.val
                right_child.val = temp
            dfs(left_child.left, right_child.right, level + 1)
            dfs(left_child.right, right_child.left, level + 1)
        dfs(root.left, root.right, 0)
        return root
        # time complexity: O(n) do O(1) work swapping children values and visit every node in tree once
        # space: O(log n) call stack is the height of perfect binary tree 