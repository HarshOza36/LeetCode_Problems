class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict_s,char_dict_t = {},{}
        result_str1, result_str2 = "",""
        if(len(s) != len(t)):
            return False
        else:
            for i in range(len(s)):
                if(s[i] not in char_dict_s):
                    result_str1 += str(i)
                    char_dict_s[s[i]] = str(i)
                else :
                    result_str1 += char_dict_s[s[i]]
                if(t[i] not in char_dict_t):
                    result_str2 += str(i)
                    char_dict_t[t[i]] = str(i)
                else :
                    result_str2 += char_dict_t[t[i]]
            if(result_str1 == result_str2):
                return True
            else:
                return False