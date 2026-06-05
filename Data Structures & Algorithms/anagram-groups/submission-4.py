class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            group_dict[key].append(word)

        return list(group_dict.values())

        

        
        