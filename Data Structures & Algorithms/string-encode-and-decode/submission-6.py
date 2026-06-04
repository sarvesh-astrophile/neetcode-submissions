class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordlenght = int(s[i:j])
            i = j + 1
            j = i + wordlenght
            word = s[i:j]

            result.append(word)
            i = j

        return result