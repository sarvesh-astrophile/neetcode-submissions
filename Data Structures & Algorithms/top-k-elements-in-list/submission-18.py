class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, topK = defaultdict(int), defaultdict(list)
        result = []

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            topK[value].append(key)

        for i in range(len(nums), -1, -1):
            if i in topK:
                for j in topK[i]:
                    result.append(j)
                    if len(result) == k:
                        return result

        return result