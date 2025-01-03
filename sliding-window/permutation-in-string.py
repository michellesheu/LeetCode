class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Initialize frequency vectors
        s1v = [0] * 26
        for c in s1:
            s1v[ord(c) - ord('a')] += 1
        
        s2v = [0] * 26
        l = 0
        
        # Sliding window over s2
        for r in range(len(s2)):
            s2v[ord(s2[r]) - ord('a')] += 1
            
            # Check if the window size matches s1
            if r - l + 1 == len(s1):
                if s1v == s2v:  # Compare frequency vectors
                    return True
                
                # Shrink the window
                s2v[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False
