class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for word in strs:
            index = [0] * 26
            for char in word:
                index[ord(char) - ord("a")] += 1

            anagram_group[tuple(index)].append(word)


        return list(anagram_group.values())