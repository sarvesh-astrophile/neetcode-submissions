class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDic = defaultdict(int)
        for num in nums:
            numDic[num] += 1
            if numDic[num] > 1 :
                return True
            
        return False

        