class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = text.count(" ")                            
        text = [word for word in text.split(" ") if word]
        n = len(text)                                      
        if n == 1: 
            return text[0] + space * " "
        cnt = space//(n-1)
        rem = space % (n-1)
        return (" "*cnt).join(text) + " "*rem