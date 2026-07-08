class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_26, t_26 = defaultdict(int), defaultdict(int)
        haves, needs = 0, 0
        result, result_len = "", float("inf")

        for char in t:
            t_26[char] += 1

        needs = len(t_26)

        l = 0
        for r in range(len(s)):
            s_26[s[r]] += 1
            if s[r] in t_26 and s_26[s[r]] == t_26[s[r]]:
                haves += 1

            while haves == needs:
                if (r - l + 1) < result_len:
                    result_len = r - l + 1
                    result = s[l : r + 1]


                s_26[s[l]] -= 1
                if s[l] in t_26 and s_26[s[l]] < t_26[s[l]]:
                    haves -=  1

                l += 1

        return result if result_len != float('inf') else ""
