class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        
        for word in strs:
            group_key = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                group_key[index] += 1

            anagram_group[tuple(group_key)].append(word)


        return list(anagram_group.values())