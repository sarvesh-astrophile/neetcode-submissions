class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)
        largest = 0

        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1

            while ((r - l + 1) - max(s_dict.values())) > k:
                s_dict[s[l]] -= 1
                l += 1

            largest = max(r - l + 1, largest)

        return largest