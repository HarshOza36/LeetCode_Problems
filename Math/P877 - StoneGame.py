class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alex = 0
        lee = 0
        while(len(piles)>0):
            if(piles[0] > piles[-1]):
                alex += piles.pop(0)
                lee += piles.pop()
            else:
                alex += piles.pop()
                lee += piles.pop(0)
        if(alex > lee):
            return True
        else:
            return False