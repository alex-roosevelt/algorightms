class Solution:
    def findKthLargest(self, nums, k) -> int:
        self.merge_sort(nums, 0, len(nums) - 1)
        print(nums)
        return nums[-k]
    
    
    def merge_sort(self,arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
            
    def merge(self, arr, left, mid, right):
        s1 = mid - left + 1
        s2 = right - mid
        
        L = [0] * s1
        R = [0] * s2
        
        for i in range(s1):
            L[i] = arr[left + i]
            
        for j in range(s2):
            R[j] = arr[mid + j + 1]
        
        i, j, k = 0, 0, left
        
        while i < s1 and j < s2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i < s1:
            arr[k] = L[i]
            i+=1
            k+=1
        
        while j < s2:
            arr[k] = R[j]
            j+=1
            k+=1
        
            
arr = [3,2,1,5,6,4]
res = Solution().findKthLargest(arr, 2)
print(res)