class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        # parse all 4 digits and use string manipulation
        # maxPossible = num
        # num = str(num)

        # for i in range(len(num)):
        #     if num[i]== '6':
        #         newNum = num[:i] + '9' + num[i+1:]
        #     else:
        #         newNum = num[:i] + '6' + num[i+1:]
        #     maxPossible = max(maxPossible, int(newNum))
        # return maxPossible

        # Intuitive math solution
        # Max we can have is 9999
        # so we just need to replace and check all 4 digits
        if (num // 1000) == 6:
            # if we had 6xxx we just make it 9xxx
            num += 3000
        elif (num // 100) % 10 == 6:
            # if we had 96xx we make it 99xx 
            num+=300
        elif (num // 10) % 10 == 6:
            # if we had 996x we make it 999x
            num += 30
        elif num % 10 == 6:
            num += 3
        return num