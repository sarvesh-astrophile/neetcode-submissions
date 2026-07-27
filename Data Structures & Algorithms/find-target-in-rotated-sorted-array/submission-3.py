class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                result = mid
                break

            # left part
            if nums[l] <= nums[mid]:
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
        
        return result