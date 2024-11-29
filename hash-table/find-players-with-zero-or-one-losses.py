from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = []
        list1 = []
        list2 = []
        player_loss = defaultdict(int)
        for winner, loser in matches:
            player_loss[loser] += 1
        print(player_loss)
        for key, val in player_loss.items():
            if val == 1:
                list2.append(key)
        for winner, loser in matches:
            if winner not in player_loss:
                list1.append(winner)
        print(set(list1))
        print(set(list2))
        ans.append(sorted(list(set(list1))))
        ans.append(sorted(list(set(list2))))
        return ans

            
            