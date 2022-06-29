class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        res = set()
        def helper(tiles, ans):
            if ans:
                res.add(ans)
            print(ans)
            for i in range(len(tiles)):
                helper(tiles[:i] + tiles[i+1:], ans + tiles[i])
        helper(tiles, '')
        return (len(res))