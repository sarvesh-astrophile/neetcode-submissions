class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # init
        s1_26, s2_26 = [0] * 26, [0] * 26
        matches = 0

        for i in range(len(s1)):
            index1 = ord(s1[i]) - ord('a')
            s1_26[index1] += 1

            index2 = ord(s2[i]) - ord('a')
            s2_26[index2] += 1

        for i in range(26):
            if s1_26[i] == s2_26[i]:
                matches += 1

        # algo
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # right
            index1 = ord(s2[r]) - ord('a')
            if s1_26[index1] == s2_26[index1]:
                matches -= 1

            s2_26[index1] += 1
            if s1_26[index1] == s2_26[index1]:
                matches += 1

            # left
            index2 = ord(s2[l]) - ord('a')
            if s1_26[index2] == s2_26[index2]:
                matches -= 1

            s2_26[index2] -= 1
            if s1_26[index2] == s2_26[index2]:
                matches += 1

            l +=1

        return matches == 26