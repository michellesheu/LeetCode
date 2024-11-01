class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
        
        def dfs(i, j):
            nonlocal curr
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if valid(ni, nj) and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    curr += 1
                    dfs(ni, nj)
        
        # Iterate over all cells in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    curr = 1  # Start area count for a new island
                    dfs(i, j)
                    max_area = max(max_area, curr)  # Update max_area after finishing an island
        
        return max_area
