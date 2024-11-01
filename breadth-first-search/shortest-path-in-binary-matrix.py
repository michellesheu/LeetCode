from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1  # No path if start or end is blocked
        
        queue = deque([(0, 0, 1)])  # Start from (0,0) with path length 1
        grid[0][0] = 1  # Mark the starting cell as visited
        
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
        
        while queue:
            i, j, steps = queue.popleft()
            
            # If we reach the target cell, return the steps taken
            if i == n - 1 and j == n - 1:
                return steps
            
            # Explore all 8 directions
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                # If the neighbor cell is valid and unvisited
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    queue.append((ni, nj, steps + 1))
                    grid[ni][nj] = 1  # Mark as visited by setting it to 1
        
        return -1  # No path found
