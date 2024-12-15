class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        all_nines = set(digits)
        if len(all_nines) == 1 and 9 in all_nines:
            for i in range(len(digits)):
                digits[i] = 0
            digits.insert(0, 1)
            return digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                digits[i-1] += 1
            else:
                digits[i] += 1
                return digits
                
        # 9  1001
        # 10 1010
        return list(map(lambda s: int(s), list(str(int("".join(map(lambda s: str(s), digits)))+1))))
        