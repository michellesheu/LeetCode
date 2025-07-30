# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            curr_level_nodes = []
            for _ in range(level_size):
                curr_node = queue.popleft()
                curr_level_nodes.append(curr_node)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            if level % 2 == 1:
                left = 0
                right = level_size - 1
                while left < right:
                    curr_level_nodes[left].val, curr_level_nodes[right].val = curr_level_nodes[right].val, curr_level_nodes[left].val
                    left += 1
                    right -= 1
            level += 1
        return root