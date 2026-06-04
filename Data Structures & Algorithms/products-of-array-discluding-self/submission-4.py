from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)
        
        # If more than one zero, all products are zero
        if zeros > 1:
            return [0] * n
        
        # Product of all non-zero elements
        product_all = 1
        for num in nums:
            if num != 0:
                product_all *= num
        
        result = []
        if zeros == 1:
            # Exactly one zero: only that index gets product_all, others get 0
            for num in nums:
                if num == 0:
                    result.append(product_all)
                else:
                    result.append(0)
        else:
            # No zeros: use division (allowed here, but see note)
            for num in nums:
                result.append(product_all // num)  # integer division
        return result