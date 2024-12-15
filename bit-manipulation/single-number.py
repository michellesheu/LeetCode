class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for n in nums:
            single_number ^= n
        return single_number
        