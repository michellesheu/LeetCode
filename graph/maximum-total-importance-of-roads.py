class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree_arr = [0] * n
        for road in roads:
            degree_arr[road[0]] += 1
            degree_arr[road[1]] += 1
        degree_arr.sort()
        val = 1
        total_importance = 0
        for degree in degree_arr:
            total_importance += val * degree
            val += 1
        return total_importance