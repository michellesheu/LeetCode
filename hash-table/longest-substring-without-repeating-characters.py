class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: s is a string
        # output: length of longest nonempty contiguous unique characters substring 
        # use sliding window two ptrs to keep track of left and right of substring window and use a set to keep track of seen characters 
        # iterate thru s 
        # while curr ch is in seen, remove left ch from set move left 
        # add ch to set, update curr length= right-left+1 and update max len of valid window move right ptr
        # return max len of window
        max_len = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            #invalid window
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # valid window
            seen.add(s[right])
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len


