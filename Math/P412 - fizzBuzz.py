class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(n):
            val = i+1
            if(val % 3 == 0):
                if(val % 5 == 0):
                    out.append("FizzBuzz")
                else:
                    out.append("Fizz")
            elif(val % 5 == 0):
                out.append("Buzz")
            else:
                out.append(str(val))
        return out
                