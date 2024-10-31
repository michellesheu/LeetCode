from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # undirected acyclic graph
        # preprocess array of edges with hashmap to get neighbors easily
        # dfs -> find connected component 
        if source == destination:
            return True
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        def dfs(graph, node):
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True 
                elif neighbor not in seen:
                    seen.add(neighbor)
                    return dfs(graph,neighbor)
            return False
        return dfs(graph, source)
        



