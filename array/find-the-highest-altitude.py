class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        maxAlt = currAlt
        for altGain in gain:
            currAlt += altGain
            maxAlt = max(currAlt, maxAlt)
        return maxAlt