from collections import defaultdict
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique = set()
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
            else:
                return s[i]
        