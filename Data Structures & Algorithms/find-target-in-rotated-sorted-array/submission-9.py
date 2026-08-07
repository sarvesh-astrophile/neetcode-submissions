class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init
        # left part condition, right part condition
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            # left part
            if nums[mid] >= nums[l]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right part
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
