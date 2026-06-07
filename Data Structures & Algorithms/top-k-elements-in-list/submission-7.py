class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        seen = set()
        count_list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in seen:
                continue
            count = nums.count(num)
            count_list[count].append(num)
            seen.add(num)

        for i in range(len(count_list) - 1, -1, -1):
            for j in count_list[i]:
                result.append(j)
                if len(result) == k:
                    return result


        