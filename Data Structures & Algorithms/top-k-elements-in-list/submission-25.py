class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        top_k = [[] for _ in range(len(nums) + 1)]
        for key, value in count_dict.items():
            top_k[value].append(key)

        result = []
        for i in range(len(top_k) -1, -1, -1):
            for char in top_k[i]:
                result.append(char)

                if len(result) == k:
                    return result

        