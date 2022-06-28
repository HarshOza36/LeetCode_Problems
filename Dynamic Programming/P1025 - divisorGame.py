class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Smart math solution
        # return n % 2 == 0
        
        # using DP
        
        def game(n, bob):
            if(n == 1 and bob):
                return True # since it was bob's turn and there are no other choices
            
            for i in range(1,n):
                if(n % i == 0):
                    return game(n-i , not bob) # Since its alice's move. 
            return False # after all tries alice loses so bob won
        
        # Alice will start first hence bob''s move is false    
        return game(n, False)
