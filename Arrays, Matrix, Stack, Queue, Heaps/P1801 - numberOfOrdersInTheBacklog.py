class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyOrders = []
        sellOrders = []
        
        heapify(buyOrders)
        heapify(sellOrders)

        MOD = 10**9 + 7

        for price, amt, orderType in orders:
            if orderType == 0:
                currAmt = amt
                while sellOrders and sellOrders[0][0] <= price and currAmt > 0:
                    sellPrice, sellAmt = heappop(sellOrders)
                    rem = currAmt - sellAmt
                    if rem < 0:
                        heappush(sellOrders, (sellPrice, sellAmt-currAmt))
                    currAmt -= sellAmt
                if currAmt > 0:
                    heappush(buyOrders, (-price, currAmt))
            else:
                currAmt = amt
                while buyOrders and -buyOrders[0][0] >= price and currAmt > 0:
                    buyPrice, buyAmt = heappop(buyOrders)
                    rem = currAmt - buyAmt
                    if rem < 0:
                        heappush(buyOrders, (buyPrice, buyAmt-currAmt))
                    currAmt -= buyAmt
                if currAmt > 0:
                    heappush(sellOrders, (price, currAmt))

        ans = 0
        ans += sum(i[1] for i in buyOrders) % MOD
        ans += sum(i[1] for i in sellOrders) % MOD
        return ans % MOD