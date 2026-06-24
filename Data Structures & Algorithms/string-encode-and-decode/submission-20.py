class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        l, r = 0, 0
        while r < len(s):
            while s[r] != "#":
                r += 1
            wordlength = int(s[l:r])
            r = r + 1
            l = r + wordlength
            word = s[r:l]
            result.append(word)
            r = l

        return result
