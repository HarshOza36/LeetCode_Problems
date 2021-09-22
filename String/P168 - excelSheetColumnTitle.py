class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        m = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        columnTitle = ""
        while columnNumber > 0:
            columnTitle += m[(columnNumber - 1) % 26]
            columnNumber = (columnNumber - 1) // 26

        return columnTitle[::-1]
    