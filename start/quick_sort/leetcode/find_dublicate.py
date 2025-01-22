import random

class Solution:
    def findDuplicate(self, nums) -> int:
        nums = self.quick_sort(nums)
        j = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[j]:
                return nums[i]
            j+=1
    
    def quick_sort(self, arr):
        if len(arr) <=1:
            return arr
        elem = random.choice(arr)
        left = list(filter(lambda x : x < elem, arr))
        center = [i for i in arr if i == elem]
        right = list(filter(lambda x : x > elem, arr))
        return self.quick_sort(left) + center + self.quick_sort(right)
        
        
        
    
nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))