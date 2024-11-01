from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Build the graph as an undirected graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        # Initialize seen with restricted nodes
        seen = set(restricted)
        curr = 1  # Start with node 0, the source
        seen.add(0)  # Mark the starting node as seen
        
        # DFS function to explore reachable nodes from node 0
        def dfs(node):
            nonlocal curr
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    curr += 1
                    dfs(neighbor)
        
        # Start DFS from node 0 only
        dfs(0)
        
        return curr
