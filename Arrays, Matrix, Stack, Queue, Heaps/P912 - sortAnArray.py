class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) <= 1):
            return nums
        
        mid = len(nums) // 2
        l,r = nums[:mid], nums[mid:]
        return self.mergeSort(self.sortArray(l),self.sortArray(r))
    def mergeSort(self,left,right):
        sorted = [None]*(len(left) + len(right))
        i = j = k = 0
        while(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                sorted[k] = left[i]
                i += 1
            else:
                sorted[k] = right[j]
                j += 1
            k += 1
        
        while(i < len(left)):
            sorted[k] = left[i]
            i += 1
            k += 1
        while(j < len(right)):
            sorted[k] = right[j]
            j += 1
            k += 1
        return sorted