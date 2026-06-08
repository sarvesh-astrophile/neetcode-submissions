class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(set)
        result = []

        for num in nums:
            freq_dict[nums.count(num)].add(num)

        for i in range(len(nums), -1, -1):
            for j in freq_dict[i]:
                result.append(j)
                if k == len(result):
                    return result

        return result