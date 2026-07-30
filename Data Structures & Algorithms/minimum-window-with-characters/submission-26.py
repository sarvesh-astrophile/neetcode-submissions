class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # 1. init
        s_count, t_count = defaultdict(int), defaultdict(int)
        needs, haves = 0, 0
        result, result_len = "", float("inf")

        for char in t:
            t_count[char] += 1

        # 2. needs in t
        needs = len(t_count)

        # 3. finding in s
        l = 0
        for r in range(len(s)):
            # adding to dict
            index1 = s[r]
            s_count[index1] += 1

            if index1 in t_count and s_count[index1] == t_count[index1]:
                haves += 1

            # while removing
            while needs == haves:
                if (r - l + 1) < result_len:
                    result = s[l : r + 1]
                    result_len = r - l + 1

                index2 = s[l]
                if index2 in t_count and s_count[index2] == t_count[index2]:
                    haves -= 1

                s_count[index2] -= 1
                
                l += 1


        return result if result_len != float("inf") else ""
