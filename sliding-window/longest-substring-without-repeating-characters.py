class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        uniq = set()
        max_size = 0
        for right in range(len(s)):
            while s[right] in uniq:
                uniq.remove(s[left])
                left += 1
                print(right, left)
                max_size = max(right-left+1, max_size)
                print(max_size)
            uniq.add(s[right])  

        return max_size


