class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        print("".join(f'{len(s)}#{s}' for s in strs))
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            # Find the next '#'
            j = s.find('#', i)
            
            # Extract the length prefix
            str_len = int(s[i:j])
            
            # Extract the string using the length
            word = s[j+1:j+1+str_len]
            ans.append(word)
            
            # Move to the next encoded string
            i = j + 1 + str_len
        
        return ans

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))