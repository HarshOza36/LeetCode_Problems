class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(n) algorithm
        # l = 0
        # r = len(arr)
        # i = 1 # the integer values start from one
        # ans = 0
        # while k:
        #     if(l < r):
        #         if(i == arr[l]): # for the first time If first one is 1
        #             i, l = i+1, l+1 # increment the integer and the left pointer
        #         else: # If it is not
        #             res, k , i = i, k-1, i+1 # res is the value of the missing number, k is decremented since we found one missing, and then integer incremented
        #     else:
        #         res, k , i = i, k-1, i+1
        # return res
        
        # Using binary search
        l = 0
        r = len(arr) - 1
        while(l <= r):
            mid = (l + r) // 2
            if((arr[mid] - mid-1) >= k): # for example is mid = 3 and arr[3] is 6 instead of 4 because[1,2,3,4] then 6 - 3 - 1 = 2 which means 4,5 were missed after 3.
                r = mid - 1
            else:
                l = mid + 1
        if(r < 0):
            return k 
        else: 
            return (k + r+1) 