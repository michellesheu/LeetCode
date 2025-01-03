class Solution:
    def areVectorsEqual(self, a, b):
        for i in range(26):
            if a[i] != b[i]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        freqS1 = [0] * 26  # Frequency array for s1
        for c in s1:
            freqS1[ord(c) - ord('a')] += 1
        
        freqS2 = [0] * 26  # Sliding window frequency array for s2
        i, j = 0, 0  # Window pointers
        
        while j < len(s2):
            # Add current character in s2 to freqS2
            freqS2[ord(s2[j]) - ord('a')] += 1
            
            # Check if window size matches s1 length
            if j - i + 1 == len(s1):
                # If the two frequency arrays match, return True
                if self.areVectorsEqual(freqS1, freqS2):
                    return True
            
            # If the window size is less than s1, expand it by moving j
            if j - i + 1 < len(s1):
                j += 1
            else:
                # If the window size is equal to or greater than s1, shrink it
                freqS2[ord(s2[i]) - ord('a')] -= 1
                i += 1
                j += 1
        
        return False
