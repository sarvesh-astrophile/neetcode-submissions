class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        substring, sublength = "", float('inf')
        window, Tcount = defaultdict(int), defaultdict(int)
        haves, needs = 0, 0

        for i in range(len(t)):
            Tcount[t[i]] += 1

        needs = len(Tcount)

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == Tcount[s[r]]:
                haves += 1

            while haves == needs:
                if sublength > (r - l + 1):
                    substring = s[l:r + 1]
                    sublength = r - l + 1


                if window[s[l]] == Tcount[s[l]]:
                    haves -= 1
                
                window[s[l]] -= 1
                l += 1
     
        return substring 