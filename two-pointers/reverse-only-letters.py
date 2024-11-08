class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[r].isalpha():
                r -= 1
            while l < r and not s[l].isalpha():
                l += 1
            letters[r], letters[l] = letters[l], letters[r]
            l+=1
            r-=1
        return "".join(letters)