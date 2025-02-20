from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        even_index = 0
        odd_index = 1
        n = len(nums)
        
        while even_index < n and odd_index < n:
            if nums[even_index] % 2 != 0:
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
                odd_index+=2
            else:
                even_index+=2
        return nums

nums = [4,2,5,7]
print(Solution().sortArrayByParityII(nums))