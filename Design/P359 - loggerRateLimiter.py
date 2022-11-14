class Logger:
    def __init__(self):
      self.logger = {}

    def shouldPrintMessage(self, timestamp, message):
      if message in self.logger:
        if timestamp - self.logger[message] < 10:
          return False
      self.logger[message] = timestamp
      return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp, message)

obj = Logger()
param_1 = obj.shouldPrintMessage(1, "foo")
param_2 = obj.shouldPrintMessage(2, "bar")
param_3 = obj.shouldPrintMessage(3, "foo")
param_4 = obj.shouldPrintMessage(8, "bar")
param_5 = obj.shouldPrintMessage(10, "foo")
param_6 = obj.shouldPrintMessage(11, "foo")
print([param_1, param_2, param_3, param_4, param_5, param_6])