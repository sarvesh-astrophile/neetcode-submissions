class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # init
        small, big = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(small) + len(big)
        half = total // 2

        # find perfect half
        l, r = 0, len(small) -1
        while True:
            # index of small and big
            i = l + (r - l) // 2
            j = half - i - 2

            # varibles
            left_small = small[i] if i >= 0 else float('-inf')
            right_small = small[i + 1] if (i + 1) < len(small) else float('inf')

            left_big = big[j] if j >= 0 else float('-inf')
            right_big = big[j + 1] if (j + 1) < len(big) else float('inf')

            # perfect half
            if left_small <= right_big and right_small >= left_big:
                # odd
                if total % 2:
                    return min(right_small, right_big)
                else:
                    return (max(left_small, left_big) + min(right_small, right_big)) / 2
            # not perfect half
            elif left_small > right_big:
                r = i - 1
            else:
                l = i + 1

        