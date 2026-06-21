class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

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

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx_r = ord(s2[r]) - ord('a')
            if s2_26[idx_r] == s1_26[idx_r]:
                matches -= 1

            s2_26[idx_r] += 1
            if s2_26[idx_r] == s1_26[idx_r]:
                matches += 1

            idx_l = ord(s2[l]) - ord('a')
            if s2_26[idx_l] == s1_26[idx_l]:
                matches -= 1
            
            s2_26[idx_l] -= 1
            if s2_26[idx_l] == s1_26[idx_l]:
                matches += 1

            l += 1

        return matches == 26