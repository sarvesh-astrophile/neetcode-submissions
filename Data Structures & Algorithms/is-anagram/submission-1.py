class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else: sDict[char] += 1

        for char in t:
            if char not in tDict:
                tDict[char] = 1
            else: tDict[char] += 1

        return sDict == tDict
