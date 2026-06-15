class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # func = len(str) - len(max) < k
        longest = 0
        s_dict = defaultdict(int)
        maxf = 0

        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1
            maxf = max(s_dict[s[r]], maxf)

            while ((r - l + 1) - maxf) > k:
                s_dict[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))


        return longest