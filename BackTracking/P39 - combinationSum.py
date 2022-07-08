class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(candidates, target, out, ans):
            if(target < 0):
                return
            elif(target == 0):
                ans.append(out)
                return
            for idx, c in enumerate(candidates):
                dfs(candidates[idx:], target - c, out + [c], ans)
        dfs(candidates, target, [], ans)
        return ans