class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        k_list = []
        result = []

        for i in range(k):
            k_list.append(nums[i])

        k_list.sort()
        
        l, current_max = 0, k_list[-1]
        result.append(current_max)
        for r in range(k, len(nums)):
            k_list.append(nums[r])
            current_max = max(current_max, nums[r])

            k_list.remove(nums[l])
            if nums[l] == current_max:
                current_max = sorted(k_list, reverse=True)[0]
            l += 1

            result.append(current_max)

        return result
