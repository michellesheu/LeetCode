from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def is_valid(row,col):
            return 0<=row<m and 0<= col < n
        matrix = [row[:] for row in mat]
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        seen = set()
        queue = deque()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    queue.append((row,col, 0))
                    seen.add((row, col))
        while queue:
            row,col,dist = queue.popleft()
            for dx, dy in directions:
                if is_valid(row+dx,col+dy) and (row+dx,col+dy) not in seen:
                    matrix[row+dx][col+dy] = dist + 1
                    queue.append((row+dx,col+dy,dist+1))
                    seen.add((row+dx,col+dy))
        return matrix

