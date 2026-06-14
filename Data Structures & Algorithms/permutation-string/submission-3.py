from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_26 = defaultdict(int)
        s2_26 = defaultdict(int)

        # Build frequency for s1 and the first window of s2
        for i in range(len(s1)):
            s1_26[s1[i]] += 1
            s2_26[s2[i]] += 1

        # Count initial matches (only for characters present in s1)
        matches = 0
        required = len(s1_26)          # distinct characters we care about
        for char in s1_26:
            if s1_26[char] == s2_26[char]:
                matches += 1

        # Check the very first window
        if matches == required:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # --- Add the right character ---
            right_char = s2[r]
            if right_char in s1_26:
                if s2_26[right_char] == s1_26[right_char]:
                    matches -= 1
                s2_26[right_char] += 1
                if s2_26[right_char] == s1_26[right_char]:
                    matches += 1
            else:
                s2_26[right_char] += 1

            # --- Remove the left character ---
            left_char = s2[l]
            if left_char in s1_26:
                if s2_26[left_char] == s1_26[left_char]:
                    matches -= 1
                s2_26[left_char] -= 1
                if s2_26[left_char] == s1_26[left_char]:
                    matches += 1
            else:
                s2_26[left_char] -= 1

            l += 1

            if matches == required:
                return True

        return False