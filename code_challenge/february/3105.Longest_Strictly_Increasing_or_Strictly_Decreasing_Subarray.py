# You are given an array of integers nums. Return the length of the longest 
# subarray
#  of nums which is either 
# strictly increasing
#  or 
# strictly decreasing
# .

 

# Example 1:

# Input: nums = [1,4,3,3,2]

# Output: 2

# Explanation:

# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

# Hence, we return 2.

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len, dec_len,inc_len = 1,1,1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len+=1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                dec_len +=1
                inc_len = 1
            else:
                inc_len = dec_len = 1
            
            max_len = max(max_len, inc_len, dec_len)
        return max_len
                
            

nums = [1,4,3,3,2]
print(Solution().longestMonotonicSubarray(nums))