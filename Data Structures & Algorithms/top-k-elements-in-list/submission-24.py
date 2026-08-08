class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init with count
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

        # frequency list
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in num_count.items():
            freq[value].append(key)

        # result loop
        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
