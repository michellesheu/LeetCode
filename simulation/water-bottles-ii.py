class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        max_bottles = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            empty += 1
            max_bottles += 1
        return max_bottles