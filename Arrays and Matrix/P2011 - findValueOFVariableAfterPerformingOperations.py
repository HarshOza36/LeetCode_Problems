class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for op in operations:
            if op == "--X" or op == "X--":
                x -= 1
            if op == "++X" or op == "X++":
                x += 1
        return x