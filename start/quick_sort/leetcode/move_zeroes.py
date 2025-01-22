class Solution:
    def moveZeroes(self, nums) -> None:
        if len(nums) <= 1:
            return nums
        
        n = len(nums)
        j = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
    
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)