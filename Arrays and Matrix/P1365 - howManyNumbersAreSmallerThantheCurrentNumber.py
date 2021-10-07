class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute force
        # out = []
        # for i in nums:
        #     c = 0
        #     for j in nums:
        #         if(i > j):
        #             c += 1
        #     out.append(c)
        # return out
        
        cnt = [0]*101
        out = [0]*101
        
        for num in nums:
            cnt[num] += 1
        
        tmp = 0
        for i in range(len(cnt)):
            out[i] = tmp
            tmp += cnt[i]
        x = []
        for i in nums:
            x.append(out[i])
        
        return x
        
        
            