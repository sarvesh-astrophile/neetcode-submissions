class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = set()

        l, r = 0, 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            result = max(result, r - l + 1)
            r += 1

        return result