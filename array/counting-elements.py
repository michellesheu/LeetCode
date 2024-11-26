class Solution:
    def countElements(self, arr: List[int]) -> int:
        no_dupes = set(arr)
        count = 0
        # handles counting duplicates separately
        for num in arr:
            if num + 1 in no_dupes:
                count += 1
        return count
