class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                key[index] += 1

            result[tuple(key)].append(word)

        return list(result.values())