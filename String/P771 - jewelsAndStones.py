class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        seen = set()
        for i in jewels:
            seen.add(i)
        count = 0
        for j in stones:
            if(j in seen):
                count += 1
        return count
        