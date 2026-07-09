class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        maxL = 0

        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                if s[l] in char_set:
                    char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            maxL = max(maxL, r - l + 1)

        return maxL