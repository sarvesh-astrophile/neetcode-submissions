class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            if s[r] not in seen:
                seen.add(s[r])
                length = r - l + 1
                longest = max(length, longest)

        return longest