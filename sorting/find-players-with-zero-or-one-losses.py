class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_losses = set()
        one_loss = set()
        more_losses = set()
        for winner, loser in matches:
            print(f'{winner} {loser}')
            if winner not in one_loss or winner not in more_losses:
                zero_losses.add(winner)
            elif loser not in one_loss or loser not in more_losses:
                zero_losses.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            print(f'{zero_losses}, {one_loss}, {more_losses}')
            
        return sorted([list(zero_losses), list(one_loss)])