class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # we will sort the tasks in the ascending order as per the minimum
        # energy that is required to finidh that task
        tasks.sort(key = lambda x: x[1] - x[0])
        out = 0
        for actual, minimum in tasks:
            # now the minimum energy will be the max of
            # sum of energy spent for completing prev and current task or
            # the minimum energy required to complete current task
            out = max(out + actual, minimum)
        return out