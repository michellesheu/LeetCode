class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [0] * 26
        for i in range(len(sentence)):
            letters[ord(sentence[i])-ord("a")] += 1
        for i, val in enumerate(letters):
            if val < 1:
                return False
        return True