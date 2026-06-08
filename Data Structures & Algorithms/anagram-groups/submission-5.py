class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            anagram_group = [0] * 26

            for char in word:
                char_index = ord(char) - ord("a")
                anagram_group[char_index] += 1

            result[tuple(anagram_group)].append(word)

        return list(result.values())