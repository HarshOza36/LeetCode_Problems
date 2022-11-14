class StockSpanner(object):

    def __init__(self):
        self.stack = [[float('inf'),0]] # price, day

    def next(self, price):
        currDay = self.stack[-1][1] + 1

        # we will pop all the values that are smaller than the current
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        # we will take the day difference
        res = currDay - self.stack[-1][1]

        # we will store the current day with the price
        self.stack.append([price,currDay])
        print(self.stack)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)