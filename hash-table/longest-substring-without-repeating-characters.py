class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the index of each character
        start = 0        # Start of the current substring
        max_length = 0   # Length of the longest substring found

        for end, char in enumerate(s):
            # If we've seen this character before and it's in the current substring
            if char in char_index and char_index[char] >= start:
                # Move the start to the right of the last occurrence of this character
                start = char_index[char] + 1
            else:
                # Update max_length if current substring is longer
                max_length = max(max_length, end - start + 1)
            
            # Update the last seen index of this character
            char_index[char] = end

        return max_length