class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: s is a string of alphanumeric(letters and numbers)and non-alphanumeric chars
        # output: true if palindrome all lowercase and alphanumeric chars match back and forward else false 
        # brute force: 
        # 2 ptrs: convert all uppercase chs to lowercase and check if not alpha num move ptrs to alphanum ch, if alphanum and match backward to forward, decrement right ptr and increment left ptr, if not = then return false immediately, return true at end of for loop
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            # now left and right are at alpha num chs
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            