class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])
                    break
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return ans