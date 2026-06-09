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
            wordlength = int(s[i:j])
            start = j + 1
            i = start + wordlength
            word = s[start:i]
            result.append(word)

        return result
