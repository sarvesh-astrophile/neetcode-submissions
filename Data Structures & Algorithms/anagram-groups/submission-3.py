class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_set = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            group_set[tuple(count)].append(s)

        return list(group_set.values())
