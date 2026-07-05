class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_26, t_26 = defaultdict(int), defaultdict(int)
        needs, haves = 0, 0
        result, result_length = "", float("inf")

        for char in t:
            t_26[char] += 1

        needs = len(t_26)

        l = 0
        for r in range(len(s)):
            index1 = s[r]
            s_26[index1] += 1
            if index1 in t_26 and s_26[index1] == t_26[index1]:
                haves += 1

            while needs == haves:
                if result_length > (r - l + 1):
                    result = s[l: r + 1]
                    result_length = r - l + 1

                index2 = s[l]
                s_26[index2] -= 1
                if index2 in t_26 and s_26[index2] < t_26[index2]:
                    haves -= 1

                l += 1


        return result if result_length != float("inf") else ""