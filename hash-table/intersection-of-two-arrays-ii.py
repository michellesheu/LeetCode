class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq = Counter(nums1)
        num2_freq = Counter(nums2)
        ans = []
        if len(nums1) > len(nums2):
            for n in nums2:
                if n in num1_freq:
                    num1_freq[n] -= 1
                    ans.append(n)
                    if num1_freq[n] == 0:
                        del num1_freq[n]
        else:
            for n in nums1:
                if n in num2_freq:
                    num2_freq[n] -= 1
                    ans.append(n)
                    if num2_freq[n] == 0:
                        del num2_freq[n]
        return ans 


