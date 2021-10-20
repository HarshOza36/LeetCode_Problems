class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [i for i in s if i != ""]
        return " ".join(s[::-1])