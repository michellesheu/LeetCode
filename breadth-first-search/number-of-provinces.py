from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        graph = defaultdict(list)
        
        # Build the graph correctly based on isConnected matrix
        for i in range(m):
            for j in range(i+1, m):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        count = 0
        
        # DFS to visit all nodes in the same component
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        # Traverse each node and start a DFS if not visited
        for i in range(m):
            if i not in seen:
                seen.add(i)
                dfs(i)
                count += 1  # New component/province found
        
        return count
