class Solution:
    def countElements(self, arr: List[int]) -> int:
        no_dupes = set(arr)
        count = 0
        for num in no_dupes:
            if num + 1 in no_dupes:
                count += 1
        return count
