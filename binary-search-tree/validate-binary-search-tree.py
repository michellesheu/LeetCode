# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        sorted_ans = sorted(ans)
        print(ans, sorted_ans)
        return ans == sorted_ans

        # [1,2,3]
        # [1,2,3]
        # sorted == curr_tree