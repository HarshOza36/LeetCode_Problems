class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Hard coding
        # roman = ""
        
        # thousands = ["","M","MM","MMM"]
        # hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        # tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        # ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        # ones_dig = num%10
        # tens_dig = int(num%100/10)
        # hundreds_dig = int(num%1000/100)
        # thousands_dig = int(num%10000/1000)
        
        # roman =  thousands [thousands_dig] + hundreds[hundreds_dig] + tens[tens_dig] + ones[ones_dig]
            
        # return roman
        
        # Dynamically
        out = ""
        romans  = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for key in keys:
            if(key <= num):
                cnt = num // key
                num -= key * cnt
                out += romans[key] * cnt
        return out
        
         