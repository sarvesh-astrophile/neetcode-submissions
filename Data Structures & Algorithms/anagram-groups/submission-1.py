class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for word in strs:
            key =tuple(sorted(list(word)))
            str_dict[key].append(word)
        
        return list(str_dict.values())