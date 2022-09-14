class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # find num of bytes of each number
        # Check if next n-1 bytes start with "10" if not return False
        # else return True
        i = 0
        while i < len(data):
            num = data[i]
            numBytes = 0
            if num >= 255:
                # the 9th bit is 1, we consider only 8
                return False
            elif num & 128 == 0:
                # if the first bit is 0, then num of bytes in UTF8 is 1
                numBytes = 1
            elif num & 224 == 192:
                # 224 = 11100000 if we get 192 that is 11000000
                # then this is our 2 byte UTF 8
                numBytes = 2
            elif num & 240 == 224:
                # 240 = 11110000 if we get 224 that is 11100000
                # then this is our 3 byte UTF 8
                numBytes = 3
            elif num & 248 == 240:
                numBytes = 4
            else: 
                return False
            
            for j in range(1, numBytes):
                if i+j >= len(data):
                    return False
                elif data[i+j] & 192 != 128:
                    # Checks if next one starts with 10 or not
                    return False
            i += numBytes
        return True