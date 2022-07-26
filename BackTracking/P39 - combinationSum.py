class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
       # O(len(candidates)^ target)
        ans = []
        # def dfs(candidates, target, out, ans):
        #     if(target < 0):
        #         return
        #     elif(target == 0):
        #         ans.append(out)
        #         return
        #     for idx, c in enumerate(candidates):
        #         dfs(candidates[idx:], target - c, out + [c], ans)
        # dfs(candidates, target, [], ans)

        # since its same as Subsets, lets use that code and add new conditions
        def dfs(i, cur, total):
            if total == target:
                ans.append(cur[::])
                return
            if i >= len(candidates) or total > target:
                return
            
            # Include element unlimited times
            cur.append(candidates[i])
            # for unlimited times, we dont increment i as we did in subsets
            # to include
            dfs(i, cur, total + candidates[i])
            
            # Exclude element and move ahead
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return ans
