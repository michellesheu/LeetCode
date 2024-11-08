class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt = 0
        maxAlt = float('-inf')
        for altGain in gain:
            maxAlt = max(currAlt, maxAlt)
            currAlt += altGain 
        return maxAlt