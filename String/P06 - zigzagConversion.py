class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Bruteforce - VerySlow O(numRows * n) time and space
        # if numRows == 1:
        #     return s

        # n = len(s)
        # numCols = ceil(n / (2 * numRows - 2)) * (numRows - 1)
        # cols = [[""]*(numCols) for _ in range(numRows)]

        # i = 0
        # j = 0

        # temp = 0
        # dirr = 1 # 1 = down, 0 = up
        # while temp != n:

        #     cols[i][j] = s[temp]
        #     temp += 1
            
        #     if i == numRows - 1: dirr = 0
        #     if i == 0: dirr = 1
            
        #     if dirr == 1: i += 1
        #     else: i -= 1
        
        #     if dirr == 0:
        #         j += 1
        
        # zigzag = ""

        # for i in range(numRows): 
        #     for j in range(numCols):
        #         if len(zigzag) == n: break
        #         if cols[i][j] != '':
        #             zigzag += cols[i][j]
        # return zigzag


        # O(n) solution by traversing just the string
        if numRows == 1: return s

        zigzag = ""
        n = len(s)
        section = 2 * (numRows - 1)

        for row in range(numRows):
            idx = row
            while idx < n:
                zigzag += s[idx]

                # If current row is not the first or last row then we have to add more
                #  characters in the current section
                if row != 0 and row != numRows - 1:
                    chars_in_between = section - 2 * row
                    nextIdx = idx + chars_in_between
                    
                    if nextIdx < n:
                        zigzag += s[nextIdx]

                idx += section
                
        return zigzag