from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        freq_count = defaultdict(int)
        found = False
        # freq_count = Counter(grid)
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                freq_count[grid[i][j]] += 1
        print(freq_count)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if freq_count[grid[i][j]] == 2:
                    ans.append(grid[i][j])
                    found = True
                    break
            if found:
                break
        print(ans)
        for i in range(1, n+1):
            if i not in freq_count:
                ans.append(i)
        return ans
        

