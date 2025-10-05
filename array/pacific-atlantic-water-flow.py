class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d_row = [0,0,-1,1]
        d_col = [-1,1,0,0]
        def is_valid(row, col, visited):
            return 0 <= row < n and 0 <= col < m and not visited[row][col]
        
        def dfs(row, col, arr, visited):
            for i in range(len(d_row)):
                neighbor_row = row + d_row[i]
                neighbor_col = col + d_col[i]
                if is_valid(neighbor_row, neighbor_col, visited) and heights[neighbor_row][neighbor_col] >= heights[row][col]:
                    arr[neighbor_row][neighbor_col] = 1
                    visited[neighbor_row][neighbor_col] = True
                    dfs(neighbor_row, neighbor_col, arr, visited)

        n, m = len(heights), len(heights[0])
        pacific = [[0] * m for _ in range(n)]
        atlantic = [[0] * m for _ in range(n)]
        visited_p = [[False] * m for _ in range(n)]
        visited_a = [[False] * m for _ in range(n)]
        for i in range(m):
            pacific[0][i] = 1
            visited_p[0][i] = True
            atlantic[-1][i] = 1
            visited_a[-1][i] = True
            dfs(0, i, pacific, visited_p)
            dfs(n-1, i, atlantic, visited_a)

        for i in range(n):
            pacific[i][0] = 1
            visited_p[i][0] = True
            atlantic[i][-1] = 1
            visited_p[i][-1] = True
            dfs(i, 0, pacific, visited_p)
            dfs(i, m-1, atlantic, visited_a)
        result = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
        return result

                

                

        
        