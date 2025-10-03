class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # always gonna drink full bottles initially to get empty bottles to exchange
        # set empty bottles to full bottles drunk
        # set full to 0 bc drunk
        # check while num_empty >= num_exchange or num_full > 0
        # if true: exchange numExchange for one full bottle num_empty- num_exchange num_exchange ++ full_bottle ++
        # if false: drink the full bottles add to max_bottles add to empty bottles

        # initial drinking
        max_bottles = numBottles
        num_empty = numBottles
        num_full = 0
        while num_empty >= numExchange:
            print(f"{num_empty=}")
            print(f"{numExchange=}")
            print("---------------")
            num_empty -= numExchange
            numExchange += 1
            num_full += 1
            print(f"{num_full=}")
            print(f"{num_empty=}")
            print(f"{numExchange=}")
            print("---------------")
            print("---------------")
            # need to drink to exchange
            if num_full > 0 and num_empty < numExchange:
                max_bottles += num_full
                num_empty += num_full
                num_full = 0
                print("we drinking")
                print(f"{num_full=}")
                print(f"{num_empty=}")
                print(f"{numExchange=}")
                print(f"{max_bottles=}")
            
        return max_bottles