class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # handle index out of bounds and move pointers to alnum chs
            while not s[left].isalnum():
                print(f"{left=}")
                left += 1
                print(f"{left=}")
            while not s[right].isalnum():
                print(f"{right=}")
                right -= 1
                print(f"{right=}")
            # handle matching alnum and lowercase
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True