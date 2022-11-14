class StockPrice:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.timestamps = {}
        self.currTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        # we will just replace the timestamp price
        self.timestamps[timestamp] = price
        self.currTimestamp = max(self.currTimestamp, timestamp)
        
        # and add them to our heaps
        # so heaps may have multiple prices with same timestamps
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))


    def current(self) -> int:
        return self.timestamps[self.currTimestamp]

    def maximum(self) -> int:
        # get the max price with timestamp
        price, timestamp = heappop(self.maxHeap)
        # now since we can have multiple prices for same timestamp
        # we need to make sure the price we have currently is there in the 
        # actual timestamps
        while -price != self.timestamps[timestamp]:
            price, timestamp = heappop(self.maxHeap)
        # once we get the actual maximum price we save it again and return
        heappush(self.maxHeap, (price, timestamp))
        return -price

    def minimum(self) -> int:
        # same logic as maximum
        price, timestamp = heappop(self.minHeap)
        while price != self.timestamps[timestamp]:
            price, timestamp = heappop(self.minHeap)
        heappush(self.minHeap, (price, timestamp))
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()