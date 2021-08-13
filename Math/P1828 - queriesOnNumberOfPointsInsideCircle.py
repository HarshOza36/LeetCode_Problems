class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = [0 for i in range(len(queries))]
        i = 0
        for x,y,r in queries:
            for xi,yi in points:
                distance = (x-xi)**2 + (y-yi)**2
                if(distance <= r**2):
                    ans[i] += 1
            i += 1
        return ans