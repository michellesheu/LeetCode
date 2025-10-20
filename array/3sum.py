class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            curr = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == -curr:
                    if [curr, nums[j], nums[k]] not in res:
                        res.append([curr, nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -curr:
                    j += 1
                else:
                    k -= 1
        return res