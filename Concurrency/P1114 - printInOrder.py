class Foo(object):
    def __init__(self):
        self.firstThread = False
        self.secondThread = False


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstThread = True


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.firstThread:
            pass # Stuck in an infinite loop until we get first is called 
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondThread = True
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.secondThread:
            pass # Stuck in an infinite loop until we get second is called 
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()