class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) +1)]
        count_dict = defaultdict(int)
        result = []

        for num in nums:
            count_dict[num] += 1

        for key, value in count_dict.items():
            freq[value].append(key)

        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result