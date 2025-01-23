class Solution:
    # def sortColors(self, nums) -> None:
        
    #     if len(nums) <= 1:
    #         return
        
    #     start, end, i = 0, len(nums) - 1, 0
        
    #     while i <= end and start < end:
    #         if nums[i] == 0:
    #             nums[i] = nums[start]
    #             nums[start] = 0
    #             i+=1
    #             start+=1
    #         elif nums[i] == 2:
    #             nums[i] = nums[end]
    #             nums[end] = 2
    #             end-=1
    #         else:
    #             i+=1
    
    # Algorithm Dutch National Flag - is pretty cool O(n)
    def sortColors(self, nums) -> None:
        if len(nums) <= 1:
            return
        low, mid, high = 0 ,0, len(nums) -1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -=1
            else:
                mid+=1
                


nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)