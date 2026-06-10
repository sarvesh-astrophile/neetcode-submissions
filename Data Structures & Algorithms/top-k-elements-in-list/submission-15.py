class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)
        list_nums = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            list_nums[freq].append(num)

        for i in range(len(list_nums) - 1, -1, -1):
            for j in list_nums[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result