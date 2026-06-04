class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        topK = []
        
        for num in nums:
            dic[num] += 1
            
        items = list(dic.items())
        items.sort(key=lambda item: item[1], reverse=True)

        topK = [item[0] for item in items[:k]]

        return topK

    def get_value(item):
        return item[1]