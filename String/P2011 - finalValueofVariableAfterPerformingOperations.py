class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for op in operations:
            X = X + 1 if("+" in op) else X - 1
        return X