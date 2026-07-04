class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxL, maxF = 0, 0

        # lenght - max <= k
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1

            maxL = max(maxL, r - l + 1)

        return maxL