class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        uniq = set()
        max_size = 1
        if not s:
            return 0
        for right in range(len(s)):
            print(right, s[right], uniq)
            while s[right] in uniq:
                uniq.remove(s[left])
                left += 1
                print(right, left)
            uniq.add(s[right])  
            max_size = max(right-left+1, max_size)
            print(max_size)
        return max_size


