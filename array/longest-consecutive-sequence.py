class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Store all numbers in a Hash Set for $O(1)$ lookups.
        # Iterate through the set.
        # Identify the start of a sequence by checking if $x-1$ is missing from the set.
        # Count the streak for starters only by checking for $x+1, x+2, \dots$ until the chain breaks.
        # Update the maximum length found so far.
        uniq_nums = set(nums)
        max_len = 0
        for num in uniq_nums:
            # check if num is start of seq
            if num - 1 not in uniq_nums:
                cons_len = 1
                # check if consecutive element in set
                while num + 1 in uniq_nums:
                    cons_len += 1
                    num += 1
                max_len = max(max_len, cons_len)
        return max_len
                

