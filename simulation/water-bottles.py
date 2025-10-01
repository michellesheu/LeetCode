class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # input: full bottles, # empty bottles to get one full bottle
        max_bottles = numBottles
        num_empty = max_bottles 
        while num_empty >= numExchange:
            num_full = numBottles//numExchange
            print(f"{num_full=}")
            max_bottles += num_full
            print(f"{max_bottles=}")
            num_empty = numBottles%numExchange + num_full
            print(f"{num_empty=}")
            numBottles = num_empty
            print(f"{numBottles =}")
        return max_bottles