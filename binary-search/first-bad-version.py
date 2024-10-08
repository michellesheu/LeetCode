# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # n versions [1, 2, ..., n]
        # find out the first bad one, which causes all the following ones to be bad.
        # API bool isBadVersion(version) which returns whether version is bad
        # minimize the number of calls to the API.
        # binary search 
        # 1 2 3 4 5
        lo = 1
        hi = n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo