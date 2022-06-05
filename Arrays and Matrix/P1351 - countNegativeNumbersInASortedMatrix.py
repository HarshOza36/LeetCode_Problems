class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # we start from bottom right
#         m, n = len(grid), len(grid[0])
#         l, r = m-1, 0
#         cnt = 0
        
#         while(l >= 0 and r >=0 and l < m and r < n):
#             if(grid[l][r] < 0):
#                 # If an element of row is negative, all numbers after that are negative
#                 cnt += (n - r)
#                 l -= 1 # move up
#             else:
#                 r += 1 # move right to next column
#         return cnt

        # Using Binary search
        ans = 0
        n = len(grid[0])
        for row in grid:
            if(row[-1] >= 0): # This row has no negative go to next row
                continue
            elif(row[0] < 0): # First element itself is negative all ahead are negative.
                ans += n
            else:  
                l, r = 0, n-1
                while(l <= r):
                    mid = (l + r) // 2
                    if(row[mid] >= 0):
                        l += 1 
                    elif row[mid - 1] >= 0 and row[mid] < 0:
                        ans += (n - mid)
                        break
                    else:
                        r -= 1
        return ans
                