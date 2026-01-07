class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # move pointers to alnum chs
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # handle matching alnum and lowercase
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True