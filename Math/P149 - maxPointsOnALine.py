class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # we know y = mx+c and m = slope = y2-y1 / x2-x1
        # c = y - mx
        # x intercept , set y = 0 and solve for x
        # -c = mx => x = -c/m
       

        slope = lambda x1,y1,x2,y2 : (y2-y1) / (x2-x1) if x2-x1 != 0 else 1
        constant = lambda y,m,x1,x2 : (y)-(m*x1) if x2!=x1 else -x1
        x_intercept = lambda c,m : -c/m if m != 0 else 0
        

        
        ans = 1
        for i in range(len(points)):
            x1,y1 = points[i]
            sameLine = collections.defaultdict(set)
            for j in range(i+1,len(points)):
                
                x2,y2 = points[j]
                m = slope(x1,y1,x2,y2)
                c = constant(y1,m,x1,x2)
                x = x_intercept(c,m)

                sameLine[(m,c,x)].add((x1,y1))
                sameLine[(m,c,x)].add((x2,y2))
                ans = max(ans, len(sameLine[(m,c,x)]))
            print(sameLine)
        return ans

