class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0 
                
        nth_line = 2**(n-1)

        if k <= nth_line / 2:
            return self.kthGrammar(n-1, k)
        else:
            return (self.kthGrammar(n-1, k-nth_line/2) + 1) % 2