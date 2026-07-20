class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_group = defaultdict(list)

        for word in strs:
            s_26 = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                s_26[idx] += 1

            ana_group[tuple(s_26)].append(word)

        return list(ana_group.values())
