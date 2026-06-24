class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, freqK = defaultdict(int), [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] += 1

        for key, value in count.items():
            freqK[value].append(key)

        for i in range(len(freqK) -1, -1, -1):
            for j in freqK[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result