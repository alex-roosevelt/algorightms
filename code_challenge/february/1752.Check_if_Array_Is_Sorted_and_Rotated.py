# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0 # count of break
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count+=1
        
        return count <=1
    
print(Solution().check([3,4,5,1,2]))  # True
print(Solution().check([2,1,3,4]))    # False
print(Solution().check([1,2,3]))      # True
print(Solution().check([1,1,1]))      # True
print(Solution().check([2,3,4,5,1]))  # True