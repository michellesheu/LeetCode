class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 9  1001
        # 10 1010
        return list(map(lambda s: int(s), list(str(int("".join(map(lambda s: str(s), digits)))+1))))
        