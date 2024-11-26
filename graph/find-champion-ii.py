class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        is_undefeated = [True] * n
        for winner, loser in edges:
            is_undefeated[loser] = False
        champion = -1
        champion_count = 0
        for team in range(n):
            if is_undefeated[team]:
                champion = team
                champion_count += 1
        if champion_count == 1:
            return champion
        return -1

