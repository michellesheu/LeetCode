class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore Voting algo
        curr_candidate = None
        count = 0
        for n in nums:
            if count == 0:
                curr_candidate = n
            else:
                if curr_candidate == n:
                    count += 1 
                else:
                    count -= 1
        return curr_candidate