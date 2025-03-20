class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        word = []
        while w1 < len(word1) and w2 < len(word2):
            word.append(word1[w1])
            word.append(word2[w2])
            w1 += 1
            w2 += 1
        print(word)
        if w1 < len(word1):
            print(word1[w1:])
            word += word1[w1:]
        elif w2 < len(word2):
            print(f'remaining: {word2[w2:]}')
            word += word2[w2:]
        print(word)
        return "".join(word)