class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1000000007
        res = 1
        # say we have p1 and d1 now for p2 d2 we can place them
        # _ p1 _ d1 _ in these 3 spaces where spaces are 3 if we are at level 2
        # thats is (n-1)*2 + 1 
        # Now if we place p2 d2 in spot 1 we will can place d2 in same place to form
        # p2d2p1d1 or we can place it in next blanks p2p1d2d1 p2p1d1d2
        # that is in first place we have 3 combination
        # in second we have 2 and in last we have 1, since di should be after pi
        # this is basically n(n+1)/2 combinations where n is our spaces

        for i in range(2, n + 1):
            spaces = (i-1) * 2 + 1
            val = spaces * (spaces + 1)//2
            res *= val
            res %= MOD
        return res