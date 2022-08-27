class Solution:
    def sumZero(self, n: int) -> List[int]:
        # symmetric list
        ans = deque([0]) if n & 1 else deque()
        i = 1
        while len(ans) != n:
            ans.append(i)
            ans.appendleft(-i)
            i += 1
        return ans
        
        # python one liner, assymetric list
        # return list(range(1,n)) + [-n*(n-1)//2]