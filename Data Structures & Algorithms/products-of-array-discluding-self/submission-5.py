from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)
        
        if zeros > 1:
            return [0] * n
        
        product_all = 1
        for num in nums:
            if num != 0:
                product_all *= num
        
        result = []
        if zeros == 1:
            for num in nums:
                if num == 0:
                    result.append(product_all)
                else:
                    result.append(0)
        else:
            for num in nums:
                result.append(product_all // num)  
        return result