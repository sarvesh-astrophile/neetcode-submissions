class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for char in strs:
            result += str(len(char)) + "#" + str(char)

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        
        l, r = 0, 0
        while r < len(s):
            while s[r] != "#":
                r += 1

            length = int(s[l:r])
            l = r + 1
            r = r + length + 1
            word = s[l:r]
            result.append(word)
            l = r

        return result

