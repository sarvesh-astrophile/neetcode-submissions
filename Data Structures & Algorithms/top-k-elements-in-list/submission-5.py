class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, times in count.items():
            freq[times].append(num)

        result = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result