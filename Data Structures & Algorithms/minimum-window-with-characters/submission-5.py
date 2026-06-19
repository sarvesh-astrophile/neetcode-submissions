class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # init
        window, Tcount = defaultdict(int), defaultdict(int)
        needs, haves = 0, 0
        result, resultlen = [-1, -1], float('inf')

        for i in range(len(t)):
            Tcount[t[i]] += 1

        needs = len(Tcount)

        # algo
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in Tcount and window[s[r]] == Tcount[s[r]]:
                haves += 1

            while haves == needs:
                if resultlen > (r - l + 1):
                    resultlen = r - l + 1
                    result[0], result[1] = l, r

                window[s[l]] -= 1
                if s[l] in Tcount and window[s[l]] < Tcount[s[l]]:
                    haves -= 1

                l += 1

        return s[result[0]: result[1] + 1] if resultlen != float('inf') else ""