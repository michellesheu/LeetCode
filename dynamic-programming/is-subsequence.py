class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            print(f"before s[i] {s[i]} t[j] {t[j]}")
            if s[i] == t[j]:
                print(f"equal s[i] {s[i]} t[j] {t[j]}")
                i += 1
                j += 1
            else:
                print(f"not equal s[i] {s[i]} t[j] {t[j]}")
                j += 1
        return True if i == len(s) else False
        