from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        slow = 0
        
        for fast in range(1, len(nums) - 1):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
        return slow+1