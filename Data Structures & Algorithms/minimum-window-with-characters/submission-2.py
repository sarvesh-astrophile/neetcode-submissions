class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window, Tcount = defaultdict(int), defaultdict(int)
        substring, sublength = "", float('inf')
        
        # init
        for char in t:
            Tcount[char] += 1

        haves, needs = 0, len(Tcount)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == Tcount[s[r]]:
                haves += 1

            while haves == needs:
                current_len = r - l + 1
                if current_len < sublength:
                    substring = s[l:r + 1]
                    sublength = current_len

                if window[s[l]] == Tcount[s[l]]:
                    haves -= 1

                window[s[l]] -= 1
                l += 1

        return substring if sublength != float('inf') else ""
