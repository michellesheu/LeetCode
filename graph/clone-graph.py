"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone = Node(node.val, [])
        self.visited[node] = clone
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone