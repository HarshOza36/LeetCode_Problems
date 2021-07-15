class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Hard coding
        roman = ""
        
        thousands = ["","M","MM","MMM"]
        hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        ones_dig = num%10
        tens_dig = int(num%100/10)
        hundreds_dig = int(num%1000/100)
        thousands_dig = int(num%10000/1000)
        
        roman =  thousands [thousands_dig] + hundreds[hundreds_dig] + tens[tens_dig] + ones[ones_dig]
            
        return roman
         
        
         