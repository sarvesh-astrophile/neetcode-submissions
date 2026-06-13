class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = defaultdict(int)
        maxf = 0

        l, r = 0, 0
        while r < len(s):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            func = (r - l + 1) - maxf
            while func > k :
                count[s[l]] -= 1
                l += 1
                func = (r - l + 1) - maxf
            
            longest = max(longest, r - l + 1)
            r += 1

        return longest