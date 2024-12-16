class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        avg = [-1] * len(nums)
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        print(prefix)
        for i in range(k, len(prefix)-k):
            print(prefix[i+k],2*k+1)
            avg[i] = (prefix[i+k]-prefix[i-k] + nums[i-k]) // (2*k+1)
        return avg

