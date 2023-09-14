class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {i:set() for i in range(1,n+1)}

        for a,b in trust:
            d[a].add(b)

        judge = -1
        for k,v in d.items():
            if len(v) == 0:
                if judge == -1:
                    judge = k
                else:
                    judge = -1

        if judge != -1:
            for k,v in d.items():
                if k != judge and judge not in v:
                    return -1
        return judge