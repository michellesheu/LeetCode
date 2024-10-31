from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # preprocess edges with hashmap of neighbors
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # avoid cycles
        seen = set()
        count = 0
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        for node in graph:
            if node not in seen:
                seen.add(node)
                dfs(node)
                count += 1
        return count