class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == -curr:
                    res.append([curr, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] < -curr:
                    j += 1
                else:
                    k -= 1
        return res