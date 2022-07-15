class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # TLE
        
#         n = len(nums)
        
#         subset = [[] for _ in range(k)]

#         def partitionNK(idx, non_empty, subset):
#             if idx > n-1:
#                 if non_empty == k:
#                     curr_sum = 0
#                     prev_sum = sum(subset[0])
#                     for i in range(1,k):
#                         curr_sum = sum(subset[i])
#                         if prev_sum != curr_sum:
#                             return False
#                         prev_sum = curr_sum
#                     return True
#                 return False

#             for j in range(len(subset)):
#                 if len(subset[j]) > 0: # If the set already as some element
#                     subset[j].append(nums[idx]) 
#                     # we wont add new element to form new subset rather add it to 
#                     # formed one
#                     if partitionNK(idx+1, non_empty, subset):
#                         return True
#                     subset[j].pop()
#                 else:
#                     subset[j].append(nums[idx]) 
#                     # we add new element to form new subset rather add it to 
#                     # formed one
#                     if partitionNK(idx+1, non_empty+1, subset):
#                         return True
#                     subset[j].pop()
#                     break # because it will then generate permutations 
#                     # say we havd [1],[],[], if we dont break we will form [],[1],[] 
#                     # and [],[],[1] which all are same
#             return False

#         return partitionNK(0, 0, subset)


        n = len(nums)
        s = sum(nums)
        target = s//k
        if s/k != target:
            return False
        nums.sort(reverse = True)

        subset = [0]*k  
        mem = set() # memoization
        def backtrack(idx):
            if idx == n:
                return True
            symbol = '.'.join(map(str, subset))
            if symbol in mem: return False
            mem.add(symbol)
            for j in range(k):
                if subset[j] + nums[idx] <= target:
                    subset[j] += nums[idx]
                    if backtrack(idx+1):
                        return True
                    subset[j] -= nums[idx]
                    if subset[j] == 0: break 
                    
            return False
        return backtrack(0)