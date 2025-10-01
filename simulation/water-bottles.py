class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # input: full bottles, # empty bottles to get one full bottle
        max_bottles = numBottles
        num_empty = max_bottles 
        while num_empty >= numExchange:
            num_full = num_empty//numExchange
            max_bottles += num_full
            num_empty = num_empty%numExchange + num_full
        return max_bottles