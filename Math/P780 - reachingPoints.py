class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
                
            if tx == sx: # then only need to change ty
                if (ty - sy) % tx == 0:
                    return True
                else:
                    return False
                
            if ty == sy: # then only need to change tx
                if (tx - sx) % ty == 0:
                    return True
                else:
                    return False
                
        return False
                