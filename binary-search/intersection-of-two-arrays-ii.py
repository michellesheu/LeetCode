class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq = Counter(nums1)
        ans = []
        for n in nums2:
            if n in num1_freq:
                num1_freq[n] -= 1
                ans.append(n)
                if num1_freq[n] == 0:
                    del num1_freq[n]
        return ans 


