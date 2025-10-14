class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # input: nums, size
        # output: return true if valid
        n = len(nums)
        longest_increasing = 1
        first_valid = False
        for i in range(len(nums)-1):
            print(f"{nums[i]=} {nums[i+1]=}")
            print(f"{longest_increasing=}")
            if nums[i] < nums[i+1]:
                longest_increasing += 1
            if longest_increasing >= 2*k:
                print("here")
                return True
            elif nums[i] >= nums[i+1]:
                if longest_increasing >= k:
                    first_valid = True
                else:
                    first_valid = False
                longest_increasing = 1
            if first_valid and longest_increasing >= k:
                return True
        return False
            

