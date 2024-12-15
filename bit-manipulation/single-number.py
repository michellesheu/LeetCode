class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dict = Counter(nums)
        for n in nums:
            if freq_dict[n] == 1:
                return n
        