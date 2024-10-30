class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j]=='1'
        def dfs(i,j):
            for dx,dy in directions:
                if isValid(i+dx,j+dy) and (i+dx,j+dy) not in visited:
                    visited.add((i+dx,j+dy))
                    dfs(i+dx,j+dy)
        # start at 1 check 4 directions for 1 neighbors, add 1's to visited,
        # until only 0 neighbors, increment count
        m = len(grid)
        n = len(grid[0])
        visited = set()
        num_islands = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    num_islands += 1
                    dfs(i,j)
                    visited.add((i,j))
        return num_islands
                    
