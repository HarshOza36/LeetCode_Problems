class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ai = num1.index("+")
        bi = num2.index("+")
        x1, y1 = int(num1[:ai]), int(num1[ai+1:-1])
        x2, y2 = int(num2[:bi]), int(num2[bi+1:-1])
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"
        