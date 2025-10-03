import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        def valid(row, col, numOfRows, numOfCols, visited):
            return 0 <= row < numOfRows and 0 <= col < numOfCols and not visited[row][col]
        dRow = [0,0,-1,1]
        dCol = [-1,1,0,0]
        numOfRows = len(heightMap)
        numOfCols = len(heightMap[0])
        visited = [[False for _ in range(numOfCols)] for _ in range(numOfRows)]
        boundary = []
        for i in range(numOfCols):
            heapq.heappush(boundary, (heightMap[0][i], 0, i))
            heapq.heappush(boundary, (heightMap[numOfRows-1][i], numOfRows-1, i))
            visited[0][i] = True
            visited[numOfRows-1][i] = True
        for j in range(numOfRows):
            heapq.heappush(boundary, (heightMap[j][0], j, 0))
            heapq.heappush(boundary, (heightMap[j][numOfCols-1], j, numOfCols-1))
            visited[j][0] = True
            visited[j][numOfCols-1] = True
        total_water_vol = 0
        while boundary:
            min_height, curr_row, curr_col = heapq.heappop(boundary)
            min_b_height = min_height
            for i in range(4):
                neighbor_row = curr_row + dRow[i]
                neighbor_col = curr_col + dCol[i]
                if valid(neighbor_row, neighbor_col, numOfRows, numOfCols, visited):
                    if heightMap[neighbor_row][neighbor_col] < min_b_height:
                        print(f"{neighbor_row=} {neighbor_col=}")
                        print(f"before { total_water_vol=}")
                        total_water_vol += min_b_height - heightMap[neighbor_row][neighbor_col]
                        print(f"after {total_water_vol=}")
                    print(f"{heightMap[neighbor_row][neighbor_col]=}")
                    print(f"{min_b_height=}")
                    heapq.heappush(boundary, (max(heightMap[neighbor_row][neighbor_col], min_b_height), neighbor_row, neighbor_col))
                    visited[neighbor_row][neighbor_col] = True
        return total_water_vol
