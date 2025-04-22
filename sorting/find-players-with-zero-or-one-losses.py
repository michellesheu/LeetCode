class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_losses, one_loss, more_losses = set(), set(), set()

        for w, l in matches:
            # ensure winners with no losses so far
            if w not in one_loss and w not in more_losses:
                zero_losses.add(w)

            # process this loss
            if l in zero_losses:
                zero_losses.remove(l)
                one_loss.add(l)
            elif l in one_loss:
                one_loss.remove(l)
                more_losses.add(l)
            elif l not in more_losses:
                # first-ever loss
                one_loss.add(l)
            # else: l is already in more_losses, do nothing

        return [
            sorted(zero_losses),
            sorted(one_loss)
        ]
