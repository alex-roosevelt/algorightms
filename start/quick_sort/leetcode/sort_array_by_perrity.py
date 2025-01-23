from typing import List


# simple algorithm for partitioning on two subarrays with Time Complexity O(n)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]


nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))