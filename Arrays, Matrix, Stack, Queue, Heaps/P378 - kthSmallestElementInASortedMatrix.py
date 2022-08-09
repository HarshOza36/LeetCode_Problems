class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Brute force 
        # # Flatten list O(n^2)
        # matrix = sum(matrix, [])
        # # sort O(nlogn)
        # matrix.sort()
        # return matrix[k-1]
    
        # As question asked less time complexity than O(n^2)
        n = len(matrix)
        def countLessOrEqual(mid):
            cnt = 0
            row, col = 0, n - 1
            
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    # we do col+1 so it will include all elements 
                    # before that element plus itself
                    # for example, mid is 9, 
                    # col will be 2, we will add cnt = 3, so 1, 5,9 all are 
                    # added
                    cnt += col + 1
                    row += 1
                else:
                    col -= 1
            return cnt
        
        min_val, max_val = matrix[0][0], matrix[n-1][n-1]
        while min_val != max_val:
            mid = (min_val + max_val) // 2
            
            # we will count how many elements are less than or equal to
            # this element mid
            # in first iteration we will have 1+15/2 = 8
            # so we will search and count how many elements are  <= 8
            cnt = countLessOrEqual(mid)
            if cnt < k:
                min_val = mid + 1
            else:
                max_val = mid
        return min_val