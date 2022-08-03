class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Pythonic Solution
        # arr.sort(key = lambda num: (bin(num).count("1"), num))
        # return arr
    
        # Bit Manipulation and Heap
        # O(32) time to get binary count of each number because 32 bits
        def countNumberOf1s(num):
            cnt = 0
            while num:
                cnt += num & 1
                num >>= 1
            return cnt
        
        heap = []
        for num in arr:
            heappush(heap, (countNumberOf1s(num), num))
            
        ans = []
        while heap:
            ans.append(heappop(heap)[1])
        return ans