class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)
        largest = 0
        maxf = 0

        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1
            maxf = max(maxf, s_dict[s[r]])
            
            while ((r - l + 1) - maxf) > k:
                s_dict[s[l]] -= 1
                l += 1

            largest = max(r - l + 1, largest)

        return largest