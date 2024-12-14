class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        print("".join(f'{len(s)}#{s}' for s in strs))
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        print(s)
        i = 0
        ans = []
        while i < len(s):
            print(s[i])
            str_len = int(s[i])
            word = s[i+2:i+2+str_len]
            print(word)
            ans.append(word)
            i = i+2+str_len
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))