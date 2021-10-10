class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        cmn_pref = 0
        
        # Finding common prefix
        while(left != right):
            left >>= 1
            right >>= 1
            cmn_pref += 1
        
        # shifting back to get actual bit positions
        return left << cmn_pref
        