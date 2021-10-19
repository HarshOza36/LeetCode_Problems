class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Brute Force
        # if not nums2:
        #   return None
        # out = []
        # for n1 in nums1:
        #     if(n1 in nums2):
        #         idx = nums2.index(n1)
        #         flag = False
        #         for n2 in nums2[idx + 1:]:
        #             if(n2 > n1):
        #                 out.append(n2)
        #                 flag = True
        #                 break
        #         if(flag == False):
        #             out.append(-1)
        # return out
        
        # Since the problem is of stack and our brute force is just 15% faster than others 
        # we implement better solution
        if not nums2:
            return None

        d = {}
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            # Comparing top of stack with nums2[i]
            while stack and nums2[i] > stack[-1]: 
                # since element is greater we pop and add to dictionary
                d[stack.pop()] = nums2[i]         
            # adding nums2[i] to the stack because we need to find a number greater than this
            stack.append(nums2[i])                      

        for ele in stack:                           
            # if we didnt find greater number
            d[ele] = -1

        out = []
        for i in range(len(nums1)):
            out.append(d[nums1[i]])
        return out
        