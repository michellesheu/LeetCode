from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def valid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j] == 1
        m = len(grid)
        n = len(grid[0])
        queue = deque()  # Use deque for efficient BFS
        max_time = 0
        min_time = 0
        fresh_oranges = 0  # Track total fresh oranges
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # Add rotten oranges with time = 0
                elif grid[i][j] == 1:
                    fresh_oranges += 1  # Count fresh oranges
        while queue:
            i,j,time = queue.popleft()
            max_time = max(max_time, time)  # Update the max time
            for dx, dy in directions:
                next_row, next_col = i + dx, j + dy
                if valid(next_row, next_col):
                    grid[next_row][next_col] = 2  # Mark as rotten
                    fresh_oranges -= 1  # Reduce the count of fresh oranges
                    queue.append((next_row, next_col, time + 1))  # Add to queue with incremented time

        # Step 3: Check if there are any fresh oranges left
        return max_time if fresh_oranges == 0 else -1
       