class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        longest_increasing = 1
        prev_increasing  = 0
        k = 0
        for i in range(len(nums)-1):
            print(f"before: {longest_increasing=}")
            if nums[i] < nums[i+1]:
                longest_increasing += 1
            elif nums[i] >= nums[i+1]:
                print(f"after: {longest_increasing=}")
                k = max(min(longest_increasing, prev_increasing), longest_increasing//2, k)
                print(f"{k=}")
                prev_increasing = longest_increasing
                print(f"{prev_increasing=}")
                longest_increasing = 1


        return k
               
            