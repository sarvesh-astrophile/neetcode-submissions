class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # init
        window, Tcount = defaultdict(int), defaultdict(int)
        needs, haves = 0, 0
        result, resultlen = "", float('inf')

        for char in t:
            Tcount[char] += 1

        needs = len(Tcount)

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in Tcount and window[s[r]] == Tcount[s[r]]:
                haves += 1

            while haves == needs and (r - l + 1) >= len(t):
                if resultlen > (r - l + 1):
                    result = s[l:r + 1]
                    resultlen = r - l + 1

                if s[l] in Tcount and window[s[l]] == Tcount[s[l]]:
                    haves -= 1

                window[s[l]] -= 1
                l += 1


        return result if resultlen != float('inf') else ""