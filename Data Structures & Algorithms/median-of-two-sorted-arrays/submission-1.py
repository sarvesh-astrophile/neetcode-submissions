class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # init small and big
        small, big = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(big) + len(small)
        half = total // 2

        # use small and big to find 1st part, use left and right
        l, r = 0, len(small) -1
        while True:
            # index of small
            i = l + (r - l) // 2
            # index of big
            j = half - i - 2

            # edge cases
            small_left = small[i] if i >= 0 else float('-inf')
            small_right = small[i + 1] if (i + 1) < len(small) else float('inf')

            big_left = big[j] if j >= 0 else float('-inf')
            big_right = big[j + 1] if (j + 1) < len(big) else float('inf')

            # correct 1st part
            if small_left <= big_right and big_left <= small_right:
                # odd total
                if total % 2:
                    return min(big_right, small_right)
                # even
                else:
                    return (max(big_left, small_left) + min(big_right, small_right)) / 2
            # incorrect
            elif small_left > big_right:
                r = i - 1
            else:
                l = i + 1

