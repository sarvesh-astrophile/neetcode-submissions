class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window, Tcount = defaultdict(int), defaultdict(int)
        haves, needs = 0, 0
        result, resultlen = "", float('inf')

        # init
        for char in t:
            Tcount[char] += 1

        needs = len(Tcount)

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if Tcount[s[r]] == window[s[r]]:
                haves += 1

            while haves == needs:
                if resultlen > (r - l + 1):
                    result = s[l:r +1]
                    resultlen = r - l + 1

                if Tcount[s[l]] == window[s[l]]:
                    haves -= 1

                window[s[l]] -= 1
                l += 1

        return result

            